#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// URL of the Star Wars API film endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch the characters for the given movie
request(url, function (err, res, body) {
  if (err) {
    console.log('Error fetching movie data:', err);
    return;
  }

  // Parse the response body to get the list of characters
  const filmData = JSON.parse(body);

  // Check if the film data is valid
  if (!filmData.characters || filmData.characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Fetch each character by their URL
  filmData.characters.forEach(characterUrl => {
    request(characterUrl, function (err, res, body) {
      if (err) {
        console.log('Error fetching character data:', err);
        return;
      }

      // Parse the character data and print the character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
