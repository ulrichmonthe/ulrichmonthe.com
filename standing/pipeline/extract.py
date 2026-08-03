"""T2 — extraction. SPEC.md §2.3.

Reads 990-PF XML and emits one record per grant PAID. Every element path comes
from schema_map.json (T1 output); none is hardcoded here.

Two traps this handles, both found by running T1 against real filings rather
than reasoning about the schema:

1. Everything is namespaced {http://www.irs.gov/efile}. Unnamespaced lookups
   return nothing and do not error, so the failure is silent.
2. GrantOrContriApprvForFutGrp is a SIBLING of the paid-grants element with an
   identical child structure, and lists grants approved for FUTURE payment.
   Counting it invents grantee relationships that never received money.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass

from resolve import GrantRecord

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "schema_map.json")) as _fh:
    SCHEMA = json.load(_fh)

NS = SCHEMA["namespace"]
BUCKET = "https://gt990datalake-rawdata.s3.amazonaws.com"


def xml_url(object_id: str) -> str:
    return f"{BUCKET}/EfileData/XmlFiles/{object_id}_public.xml"


def _q(path: str) -> str:
    """Namespace every step of a slash path."""
    return "/".join(NS + p for p in path.split("/"))


def _text(el, path: str) -> str | None:
    if el is None:
        return None
    found = el.find(_q(path))
    return found.text.strip() if found is not None and found.text else None


@dataclass
class Filing:
    ein: str
    name: str
    tax_year: int
    period_end: str | None
    state: str | None
    accepts_unsolicited: bool
    application_info_text: str | None
    fmv_assets: float | None
    records: list[GrantRecord]
    future_grants_excluded: int


def parse(xml_bytes: bytes) -> Filing | None:
    import xml.etree.ElementTree as ET

    root = ET.fromstring(xml_bytes)

    pf = root.find(_q(SCHEMA["pf_root"]))
    if pf is None:
        return None  # not a 990-PF

    ein = _text(root, SCHEMA["filer_ein"]) or ""
    name = _text(root, SCHEMA["filer_name"]) or ""
    yr = _text(root, SCHEMA["tax_year"])
    if not yr or not yr.isdigit():
        return None

    sup = root.find(_q(SCHEMA["supplementary"]))

    # Part XV line 2 is expressed structurally: a foundation that takes
    # applications populates this group; one that does not omits it.
    app = sup.find(_q(SCHEMA["application_info"]).split(NS + "SupplementaryInformationGrp/")[-1]) if sup is not None else None
    if sup is not None and app is None:
        app = sup.find(NS + "ApplicationSubmissionInfoGrp")
    accepts = app is not None
    app_text = _text(app, SCHEMA["application_form_info"]) if app is not None else None

    records: list[GrantRecord] = []
    future = 0

    if sup is not None:
        # Excluded deliberately — approved, not paid.
        future = len(sup.findall(NS + "GrantOrContriApprvForFutGrp"))

        for g in sup.findall(NS + "GrantOrContributionPdDurYrGrp"):
            org = _text(g, SCHEMA["grant_recipient_org"])
            person = _text(g, SCHEMA["grant_recipient_person"])
            is_individual = not org and bool(person)
            raw = org or person or ""

            amt_txt = _text(g, SCHEMA["grant_amount"])
            try:
                amount = float(amt_txt) if amt_txt else 0.0
            except ValueError:
                amount = 0.0

            records.append(GrantRecord(
                filer_ein=ein,
                tax_year=int(yr),
                recipient_name_raw=raw,
                recipient_state=_text(g, SCHEMA["grant_recipient_state"]),
                amount=amount,
                purpose=_text(g, SCHEMA["grant_purpose"]) or "",
                is_individual=is_individual,
            ))

    fmv_txt = _text(root, SCHEMA["fmv_assets_eoy"])
    try:
        fmv = float(fmv_txt) if fmv_txt else None
    except ValueError:
        fmv = None

    return Filing(
        ein=ein, name=name, tax_year=int(yr),
        period_end=_text(root, SCHEMA["period_end"]),
        state=_text(root, SCHEMA["filer_state"]),
        accepts_unsolicited=accepts,
        application_info_text=app_text,
        fmv_assets=fmv,
        records=records,
        future_grants_excluded=future,
    )


def fetch(object_id: str, cache_dir: str | None = None, timeout: int = 120) -> bytes | None:
    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)
        p = os.path.join(cache_dir, f"{object_id}.xml")
        if os.path.exists(p):
            with open(p, "rb") as fh:
                return fh.read()
    req = urllib.request.Request(xml_url(object_id), headers={"User-Agent": "standing/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except (urllib.error.URLError, TimeoutError):
        return None
    if cache_dir:
        with open(os.path.join(cache_dir, f"{object_id}.xml"), "wb") as fh:
            fh.write(data)
    return data
