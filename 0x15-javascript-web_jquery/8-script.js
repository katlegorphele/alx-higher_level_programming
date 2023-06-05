$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
      var movies = data.results;
      movies.forEach(function(movie) {
        var listItem = $("<li></li>").text(movie.title);
        $("#list_movies").append(listItem);
      });
    });
  });
  