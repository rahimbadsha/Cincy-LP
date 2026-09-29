/* Cover Cincy landing page — vanilla JS, no dependencies. */
(function () {
  'use strict';

  var HUBSPOT_MEETINGS_SRC = 'https://static.hsappstatic.net/MeetingsEmbed/ex/MeetingsEmbedCode.js';
  var hasIO = 'IntersectionObserver' in window;

  /* ---------- Helpers ---------- */
  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = src;
      s.async = true;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  // Run cb once when el comes within `margin` of the viewport
  function whenNear(el, margin, cb) {
    if (!el) return;
    if (!hasIO) { cb(); return; }
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) { io.disconnect(); cb(); }
    }, { rootMargin: margin });
    io.observe(el);
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- Booking calendar (HubSpot Meetings, lazy) ---------- */
  var calendar = document.querySelector('.cc-calendar');
  var calendarRequested = false;

  function loadCalendar() {
    if (calendarRequested || !calendar) return;
    calendarRequested = true;

    var container = calendar.querySelector('.meetings-iframe-container');
    new MutationObserver(function (_, obs) {
      var iframe = container.querySelector('iframe');
      if (!iframe) return;
      obs.disconnect();
      iframe.addEventListener('load', function () { calendar.classList.add('is-loaded'); });
    }).observe(container, { childList: true, subtree: true });

    loadScript(HUBSPOT_MEETINGS_SRC).catch(function () {
      calendar.querySelector('.cc-calendar__loading').textContent =
        'Calendar failed to load. Please call (513) 800-2255 to book.';
    });
  }

  whenNear(calendar, '800px 0px', loadCalendar);

  // Any CTA pointing at #book starts loading the calendar immediately
  document.querySelectorAll('a[href="#book"]').forEach(function (a) {
    a.addEventListener('click', loadCalendar);
  });

  /* ---------- Brand video (muted autoplay, sound on tap) ---------- */
  var player = document.querySelector('.cc-player');
  var brandVideo = null; // { pause: fn } — used to stop it when a testimonial plays

  function initYouTube(el) {
    var id = el.getAttribute('data-youtube-id');
    var frame = el.querySelector('.cc-player__frame');
    var soundBtn = el.querySelector('.cc-player__sound');
    var yt;

    function create() {
      yt = new window.YT.Player(frame, {
        videoId: id,
        playerVars: {
          autoplay: 1, mute: 1, playsinline: 1, rel: 0,
          modestbranding: 1, cc_load_policy: 1, cc_lang_pref: 'en'
        },
        events: {
          onReady: function (e) { e.target.mute(); e.target.playVideo(); soundBtn.hidden = false; }
        }
      });
      brandVideo = { pause: function () { if (yt && yt.pauseVideo) yt.pauseVideo(); } };
    }

    soundBtn.addEventListener('click', function () {
      if (!yt) return;
      yt.unMute();
      yt.setVolume(100);
      yt.seekTo(0, true); // restart so the viewer hears the full message
      yt.playVideo();
      soundBtn.hidden = true;
    });

    if (window.YT && window.YT.Player) { create(); return; }
    var prev = window.onYouTubeIframeAPIReady;
    window.onYouTubeIframeAPIReady = function () { if (prev) prev(); create(); };
    loadScript('https://www.youtube.com/iframe_api');
  }

  function initMp4(el) {
    var frame = el.querySelector('.cc-player__frame');
    var soundBtn = el.querySelector('.cc-player__sound');
    var video = document.createElement('video');
    video.muted = true;
    video.autoplay = true;
    video.loop = true;
    video.playsInline = true;
    video.setAttribute('playsinline', '');
    video.preload = 'metadata';
    if (el.dataset.poster) video.poster = el.dataset.poster;
    video.src = el.dataset.src;

    if (el.dataset.captions) {
      var track = document.createElement('track');
      track.kind = 'captions';
      track.srclang = 'en';
      track.label = 'English';
      track.src = el.dataset.captions;
      track.default = true;
      video.appendChild(track);
    }
    frame.appendChild(video);
    soundBtn.hidden = false;

    soundBtn.addEventListener('click', function () {
      video.muted = false;
      video.loop = false;
      video.currentTime = 0;
      video.controls = true;
      video.play();
      soundBtn.hidden = true;
    });

    brandVideo = { pause: function () { video.pause(); } };
  }

  whenNear(player, '300px 0px', function () {
    var type = player.getAttribute('data-type');
    if (type === 'youtube') initYouTube(player);
    else if (type === 'mp4') initMp4(player);
  });

  /* ---------- Testimonials (click-to-play, lightweight) ---------- */
  document.querySelectorAll('.cc-tvideo').forEach(function (btn) {
    var id = btn.getAttribute('data-youtube-id');
    if (!id) return;
    btn.style.backgroundImage = 'url(https://i.ytimg.com/vi/' + encodeURIComponent(id) + '/hqdefault.jpg)';

    btn.addEventListener('click', function () {
      if (brandVideo) brandVideo.pause();
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) +
        '?autoplay=1&playsinline=1&rel=0&modestbranding=1&cc_load_policy=1';
      iframe.title = btn.getAttribute('aria-label') || 'Client testimonial';
      iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      iframe.allowFullscreen = true;
      btn.replaceChildren(iframe);
      btn.style.cursor = 'default';
    }, { once: true });
  });

  /* ---------- Mobile sticky CTA ---------- */
  var sticky = document.querySelector('.cc-sticky');
  var heroCta = document.getElementById('hero-cta');
  var book = document.getElementById('book');

  if (sticky && heroCta && book && hasIO) {
    var heroGone = false;
    var bookVisible = false;

    function update() {
      var show = heroGone && !bookVisible;
      sticky.classList.toggle('is-visible', show);
      sticky.setAttribute('aria-hidden', show ? 'false' : 'true');
      sticky.querySelectorAll('a').forEach(function (a) { a.tabIndex = show ? 0 : -1; });
    }

    new IntersectionObserver(function (entries) {
      var e = entries[0];
      // Only "gone" once scrolled past it (above viewport), not before reaching it
      heroGone = !e.isIntersecting && e.boundingClientRect.top < 0;
      update();
    }).observe(heroCta);

    new IntersectionObserver(function (entries) {
      bookVisible = entries[0].isIntersecting;
      update();
    }, { rootMargin: '0px 0px -30% 0px' }).observe(book);
  }
})();
