(function () {
  var PREF_KEY = 'calc-lesson-lang';

  function setLang(lang) {
    document.documentElement.lang = lang;
    document.querySelectorAll('.lang-en').forEach(function (el) {
      el.hidden = lang !== 'en';
    });
    document.querySelectorAll('.lang-th').forEach(function (el) {
      el.hidden = lang !== 'th';
    });
    var btn = document.getElementById('lang-toggle');
    if (btn) btn.textContent = lang === 'en' ? 'แปลเป็นภาษาไทย' : 'Switch to English';
    try { localStorage.setItem(PREF_KEY, lang); } catch (e) {}
  }

  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.createElement('button');
    btn.id = 'lang-toggle';
    btn.className = 'lang-toggle-btn';
    btn.addEventListener('click', function () {
      setLang(document.documentElement.lang === 'th' ? 'en' : 'th');
    });

    document.body.appendChild(btn);

    var pref = 'en';
    try { pref = localStorage.getItem(PREF_KEY) || 'en'; } catch (e) {}
    setLang(pref);
  });
})();
