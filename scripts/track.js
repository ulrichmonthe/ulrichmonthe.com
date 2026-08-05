/* Shared analytics helper.
 *
 * Every event name in one file, written as a plain English sentence so the
 * Umami dashboard reads like a description of what someone did rather than a
 * list of identifiers.
 *
 * Two rules, both load-bearing because the tools make privacy promises in
 * writing:
 *   1. Count events, never content. A pasted list of funders is recorded as
 *      "a list of 12 was pasted", never the names. The policy form records the
 *      chosen sector, never the answers.
 *   2. Nothing here identifies a person. Umami is cookieless; this file adds
 *      no identifier of its own.
 *
 * Journeys: Umami stitches pageviews into a session automatically, so the page
 * sequence is already the journey. What this adds is a name for each thing a
 * visitor DID along the way, plus a `from` property on every event so a step
 * can be read without needing the pages around it.
 */
(function () {
  'use strict';

  // Which part of the site an event happened in — attached to everything, so
  // the dashboard can answer "what do people do in the checker" directly.
  function area() {
    var p = location.pathname;
    if (p.indexOf('/live-projects/ein-checker') === 0) return 'EIN checker';
    if (p.indexOf('/live-projects/ai-policy-generator') === 0) return 'Policy generator';
    if (p.indexOf('/live-projects/funder-standing') === 0) return 'Funder standing';
    if (p.indexOf('/live-projects') === 0) return 'Live projects';
    if (p.indexOf('/foundations/') === 0) return p === '/foundations/' ? 'Foundation directory' : 'Foundation page';
    if (p.indexOf('/guides/') === 0) return 'Guide';
    if (p.indexOf('/verify/') === 0) return 'State page';
    if (p.indexOf('/notes/') === 0) return 'Note';
    if (p === '/' || p === '/index.html') return 'Homepage';
    return 'Other';
  }

  // Bucket numbers rather than recording them exactly. Sizes are what matter
  // for reading intent; the precise figure is somebody's private business.
  function size(n) {
    n = Number(n) || 0;
    if (n <= 1) return '1';
    if (n <= 10) return '2-10';
    if (n <= 50) return '11-50';
    if (n <= 200) return '51-200';
    return '200+';
  }

  function track(name, data) {
    try {
      var payload = Object.assign({ from: area() }, data || {});
      if (window.umami && typeof window.umami.track === 'function') {
        window.umami.track(name, payload);
      }
    } catch (e) { /* analytics must never break a page */ }
  }

  window.track = track;
  window.trackSize = size;

  // ---- wiring that applies everywhere, so pages stay clean ----
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '';

    // Someone reached out. The single most important event on the site.
    if (href.indexOf('mailto:') === 0) {
      var subject = '';
      var m = href.match(/subject=([^&]*)/);
      if (m) { try { subject = decodeURIComponent(m[1]); } catch (e) { subject = m[1]; } }
      track('Got in touch', { about: subject || 'no subject' });
      return;
    }
    if (href.indexOf('calendly') > -1 || href.indexOf('#contact') > -1) {
      track('Opened the contact section', {});
      return;
    }
    // Moving from a tool into a single foundation's page.
    if (href.indexOf('/foundations/') === 0 && href !== '/foundations/') {
      track('Opened a foundation page', {});
      return;
    }
    // Moving between tools — the signal that someone is evaluating the author
    // rather than using one tool.
    if (href.indexOf('/live-projects/') === 0 && area().indexOf('Live projects') !== 0) {
      var dest = href.replace('/live-projects/', '').replace(/\/$/, '') || 'index';
      if (dest !== 'index') track('Moved to another tool', { tool: dest });
    }
  }, true);
})();
