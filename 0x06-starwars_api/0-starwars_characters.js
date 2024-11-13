#!/usr/bin/node

// Require the 'request' module for making HTTP requests
const request = require('request');

// Function to make a GET request and return a Promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

// Main function to fetch movie and character data
async function main() {
  const args = process.argv;  // Get command-line arguments

  // Check if a movie ID was passed
  if (args.length < 3) {
    console.log('Usage: ./0-starwars_characters.js <movie_id>');
    return;
  }

  // Define the URL for fetching movie details based on movie ID
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

  try {
    // Fetch the movie data
    const movie = await makeRequest(movieUrl);

    // If there are no characters for this movie, exit early
    if (!movie.characters || movie.characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // For each character URL, fetch character data and print their name
    for (const characterUrl of movie.characters) {
      const character = await makeRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    // If an error occurs, print it
    console.error('Error:', error.message);
  }
}

// Execute the main function
main();
