#!/usr/bin/node
// The Mode contains Star War Chatacters API request

const request = require('request');

// Movie ID (you can pass this as a command-line argument)
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command-line argument (e.g., "3" for "Return of the Jedi").');
  process.exit(1);
}

// Define the URL for the Star Wars API films endpoint
const filmsUrl = 'https://swapi.dev/api/films/' + movieId;

// Make a GET request to fetch movie details
request(filmsUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected response status code:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    // Function to fetch character names
    const fetchCharacterNames = (urls) => {
      const characterNames = [];

      const fetchNextCharacter = (index) => {
        if (index < urls.length) {
          request(urls[index], (error, response, body) => {
            if (!error && response.statusCode === 200) {
              const characterData = JSON.parse(body);
              characterNames.push(characterData.name);
              fetchNextCharacter(index + 1);
            } else {
              console.error('Error fetching character data:', error);
            }
          });
        } else {
          // All character names have been fetched, print them
          characterNames.forEach((name) => {
            console.log(`${name}`);
          });
        }
      };

      fetchNextCharacter(0);
    };

    // Fetch and display character names
    fetchCharacterNames(characterUrls);
  }
});
