const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

function fetchAndDisplayMovies() {
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const listMoviesElement = document.getElementById('list_movies');

      data.results.forEach(film => {
        const listItem = document.createElement('li');
        listItem.textContent = film.title;
        listMoviesElement.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
}

fetchAndDisplayMovies();
