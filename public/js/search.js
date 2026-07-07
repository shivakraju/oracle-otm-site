// Search for a Topic — oracle-otm.com
(function () {
  var searchData = null;

  function loadIndex(callback) {
    if (searchData) { callback(searchData); return; }
    fetch('/search-index/index.json')
      .then(function (r) { return r.json(); })
      .then(function (data) { searchData = data; callback(data); })
      .catch(function () { searchData = []; });
  }

  function highlight(text, query) {
    if (!query) return text;
    var re = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return text.replace(re, '<mark>$1</mark>');
  }

  function doSearch(query, data, resultsEl) {
    resultsEl.innerHTML = '';
    if (!query || query.length < 2) return;

    var q = query.toLowerCase();
    var matches = data.filter(function (p) {
      return (p.title && p.title.toLowerCase().includes(q)) ||
             (p.summary && p.summary.toLowerCase().includes(q)) ||
             (p.tags && p.tags.some(function (t) { return t.toLowerCase().includes(q); }));
    });

    if (matches.length === 0) {
      resultsEl.innerHTML = '<div class="sr-none">No results found.</div>';
      return;
    }

    matches.slice(0, 10).forEach(function (p) {
      var item = document.createElement('div');
      item.className = 'sr-item';
      item.innerHTML =
        '<a href="' + p.url + '">' + highlight(p.title, query) + '</a>' +
        (p.summary ? '<div class="sr-summary">' + highlight(p.summary, query) + '</div>' : '');
      resultsEl.appendChild(item);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var input = document.getElementById('search-input');
    var results = document.getElementById('search-results');
    if (!input || !results) return;

    var timer = null;

    input.addEventListener('input', function () {
      var q = input.value.trim();
      clearTimeout(timer);
      if (q.length < 2) { results.innerHTML = ''; return; }
      timer = setTimeout(function () {
        loadIndex(function (data) { doSearch(q, data, results); });
      }, 200);
    });

    // Close results when clicking outside
    document.addEventListener('click', function (e) {
      if (!input.contains(e.target) && !results.contains(e.target)) {
        results.innerHTML = '';
        input.value = '';
      }
    });
  });
})();
