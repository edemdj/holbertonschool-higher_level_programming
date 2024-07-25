const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

function fetchCharacterName() {
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const characterElement = document.getElementById('character');
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
}

fetchCharacterName();
