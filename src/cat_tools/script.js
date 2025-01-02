document.addEventListener('DOMContentLoaded', function() {
  var searchForm = document.getElementById('search-form');
  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(searchForm);
    var request = new XMLHttpRequest();
    request.open('POST', '/search');
    request.onload = function() {
      if (request.status === 200) {
        var result = JSON.parse(request.responseText);
        var data = result.msg;

        var tbody = document.querySelector('#result tbody');
        tbody.innerHTML = '';

        for (var i = 0; i < data.length; i++) {
          var row = document.createElement('tr');
          row.innerHTML = '<td>' + data[i].title + '</td>' +
            '<td>' + data[i].des + '</td>' +
            '<td>查看下载</td>';
          tbody.appendChild(row);
        }
      } else {
        console.error('搜索失败:', request.statusText);
        alert('搜索失败，请重试！');
      }

      document.getElementById('loading').style.display = 'none';
    };

    request.onerror = function() {
      console.error('搜索失败:', request.statusText);
      alert('搜索失败，请重试！');
      document.getElementById('loading').style.display = 'none';
    };

    document.getElementById('loading').style.display = 'block';
    request.send(formData);
  });
});