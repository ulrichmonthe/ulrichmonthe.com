/* Launch list — the "tell me when the next tool is live" form in the footer.
 *
 * One file, injected above the footer on every page, for two reasons:
 *   1. The site has five different footer markups and 118 of its pages are
 *      generated. Editing markup in all of them guarantees drift; editing one
 *      file does not.
 *   2. The copy and the promise under the form should be identical everywhere.
 *      If it lives in one place it stays that way.
 *
 * Failure is the interesting case. This posts to my own API, and if that
 * endpoint is missing or unreachable the form does NOT quietly swallow the
 * address — it falls back to a pre-filled email so the person can still reach
 * me in one click. A signup form that loses signups silently is worse than no
 * form at all.
 *
 * Privacy: the email address goes to my API and nowhere else. The analytics
 * events below record THAT someone joined, never who. That matches the promise
 * printed under the form, and the promise is the point.
 */
(function () {
  'use strict';

  var API = new URLSearchParams(location.search).get('api') || 'https://api.ulrichmonthe.com';
  var MAILTO = 'umonthe1@gmail.com';
  var STORE = 'notify_email';
  var EMAIL_RE = /^[^@\s]+@[^@\s.]+\.[^@\s]{2,}$/;

  function ls(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
  function save(key, val) { try { localStorage.setItem(key, val); } catch (e) {} }
  function fire(name, data) { if (window.track) window.track(name, data || {}); }

  var CSS =
    '#notify{border-top:1px solid var(--line,var(--rule,#E2DBCB));margin-top:64px;padding:34px 0 0;' +
      'font-family:var(--sans),-apple-system,system-ui,sans-serif}' +
    // Footers set their own top margin for the gap after page content. Now that
    // this block sits between, that gap reads as a hole — close it up. The id
    // selector outranks every footer rule on the site, so no !important.
    '#notify + footer{margin-top:26px}' +
    '#notify .nx{display:grid;grid-template-columns:1fr auto;gap:26px 40px;align-items:start}' +
    '#notify h2{font-family:var(--serif),Georgia,serif;font-size:20px;font-weight:600;line-height:1.3;' +
      'margin:0 0 6px;color:var(--ink,#1C1A17);letter-spacing:-.01em}' +
    '#notify p.n-why{font-size:14.5px;line-height:1.55;color:var(--ink-soft,#5B554C);margin:0;max-width:52ch}' +
    '#notify form{display:flex;flex-wrap:wrap;gap:8px;margin:0}' +
    '#notify input[type=email]{font-family:inherit;font-size:15px;padding:11px 14px;width:250px;' +
      'border:1.5px solid var(--line,var(--rule,#E2DBCB));border-radius:9px;' +
      'background:var(--card,var(--paper-raised,#FBF9F3));color:var(--ink,#1C1A17);outline:none}' +
    '#notify input[type=email]:focus{border-color:var(--accent,#A8763E)}' +
    '#notify button{font-family:inherit;font-size:15px;font-weight:600;padding:11px 20px;border:none;' +
      'border-radius:9px;background:var(--accent,#A8763E);color:#F5F1E8;cursor:pointer}' +
    '#notify button:hover{background:var(--accent-deep,#8A5F30)}' +
    '#notify button[disabled]{opacity:.6;cursor:default}' +
    '#notify .n-fine{font-size:12.5px;line-height:1.5;color:var(--ink-soft,#5B554C);margin:9px 0 0;max-width:40ch}' +
    '#notify .n-err{font-size:13.5px;color:var(--red,#9A4A32);margin:9px 0 0;max-width:44ch;line-height:1.5}' +
    '#notify .n-err a{color:var(--red,#9A4A32);font-weight:600}' +
    '#notify .n-done{font-size:14.5px;line-height:1.55;color:var(--ink-soft,#5B554C);margin:0;max-width:44ch}' +
    '#notify .n-done b{color:var(--ink,#1C1A17)}' +
    '#notify .n-hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}' +
    '@media (max-width:720px){#notify .nx{grid-template-columns:1fr;gap:18px}' +
      '#notify input[type=email]{width:100%;flex:1 1 190px}}' +
    '@media print{#notify{display:none}}';

  // Copy lives here so every page says the same thing.
  var HTML =
    '<div class="nx">' +
      '<div>' +
        '<h2>Hear about the next tool</h2>' +
        // Deliberately no list of the current tools: it would be wrong the day
        // the next one ships, on all 186 pages at once.
        '<p class="n-why">I build these one at a time and publish them free — no account, ' +
          'no paywall. Leave your email and I\'ll write once, when the next one is live.</p>' +
      '</div>' +
      '<div>' +
        '<form novalidate>' +
          '<label class="n-hp">Leave this empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label>' +
          '<label class="n-hp" for="n-email">Your email address</label>' +
          '<input type="email" id="n-email" name="email" placeholder="you@yourorganization.org" autocomplete="email">' +
          '<button type="submit">Notify me</button>' +
        '</form>' +
        // The tools promise that nothing you type reaches a server. This form is
        // the exception, so it says so rather than letting the two sit in
        // silent contradiction.
        '<p class="n-fine">Your address is stored for this one purpose. One short email per ' +
          'new tool — nothing else, never shared, one click to stop.</p>' +
        '<p class="n-err" hidden></p>' +
      '</div>' +
    '</div>';

  function alreadyOn(email) {
    return '<div class="nx"><div>' +
      '<h2>You\'re on the launch list</h2>' +
      '<p class="n-done">I\'ll write to <b>' + email.replace(/[<>&"]/g, '') + '</b> once, when the ' +
      'next tool is live. If you\'d rather come off the list, ' +
      '<a href="mailto:' + MAILTO + '?subject=' + encodeURIComponent('Take me off the launch list') +
      '">say so here</a>.</p></div><div></div></div>';
  }

  function build() {
    // Last footer on the page — some layouts nest one, none have two siblings.
    var footers = document.querySelectorAll('footer');
    var footer = footers[footers.length - 1];
    if (!footer || !footer.parentNode || document.getElementById('notify')) return;

    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    var box = document.createElement('section');
    box.id = 'notify';

    // Match the footer's own content width: pages whose footer holds a .wrap
    // are full-bleed and need one too; the rest already sit inside a container.
    var inner = box;
    if (footer.querySelector(':scope > .wrap')) {
      inner = document.createElement('div');
      inner.className = 'wrap';
      box.appendChild(inner);
    }

    var known = ls(STORE);
    if (known && EMAIL_RE.test(known)) {
      inner.innerHTML = alreadyOn(known);
      footer.parentNode.insertBefore(box, footer);
      return;
    }

    inner.innerHTML = HTML;
    footer.parentNode.insertBefore(box, footer);
    wire(box, inner);
  }

  function wire(box, inner) {
    var form = inner.querySelector('form');
    var field = inner.querySelector('#n-email');
    var btn = inner.querySelector('button');
    var err = inner.querySelector('.n-err');

    // Someone who has used the policy generator has already given me this.
    var prior = ls('policy_email');
    if (prior && EMAIL_RE.test(prior)) field.value = prior;

    // The denominator: how many people start typing versus how many finish.
    var started = false;
    field.addEventListener('focus', function () {
      if (started) return;
      started = true;
      fire('Started the launch signup', {});
    });

    function fallback(reason) {
      var body = 'Please add me to the launch list.\n\nSeen on: ' + location.pathname;
      err.innerHTML = 'That didn\'t go through. <a href="mailto:' + MAILTO + '?subject=' +
        encodeURIComponent('Add me to the launch list') + '&body=' + encodeURIComponent(body) +
        '">Email me instead</a> and I\'ll add you by hand.';
      err.hidden = false;
      fire('Could not join the launch list', { reason: reason });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      err.hidden = true;
      var email = field.value.trim();
      if (!EMAIL_RE.test(email)) {
        err.textContent = 'Please add a valid email address.';
        err.hidden = false;
        return;
      }
      btn.disabled = true;
      btn.textContent = 'Adding…';

      fetch(API + '/notify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email,
          source_path: location.pathname,   // which page persuaded them
          website: form.website.value       // honeypot: filled means a bot
        })
      })
        .then(function (r) { return r.ok; })
        .then(function (ok) {
          btn.disabled = false;
          btn.textContent = 'Notify me';
          if (!ok) { fallback('endpoint refused'); return; }
          save(STORE, email);
          fire('Asked to hear about new tools', {});
          var target = box.querySelector('.wrap') || box;
          target.innerHTML = alreadyOn(email);
        })
        .catch(function () {
          btn.disabled = false;
          btn.textContent = 'Notify me';
          fallback('could not reach the server');
        });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
