#!/usr/bin/node

/**
 * Makes an HTTP GET request and returns a Promise that resolves
 * with the parsed JSON response or rejects with an error.
 * 
 * @param {string} url - The URL to fetch.
 * @returns {Promise<Object>} A Promise that resolves with the parsed JSON response.
 */
function makeRequest(url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

/**
 * Main function that retrieves information about Star Wars movie characters
 * based on the movie ID passed as a command-line argument.
 * 
 * The movie ID is used to fetch data about the movie and its characters,
 * then it prints each character's name in the order they appear in the movie.
 */
async function main() {
  const args = process.argv;  // Retrieve command-line arguments

  // Check if movie ID is provided
  if (args.length < 3) {
    console.log('Usage: ./0-starwars_characters.js <movie_id>');
    return;
  }

  // Construct the movie URL using the passed movie ID
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

  try {
    // Fetch movie data
    const movie = await makeRequest(movieUrl);

    // If the movie has no characters, exit early
    if (!movie.characters || movie.characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // Fetch and print each character's name
    for (const characterUrl of movie.characters) {
      const character = await makeRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    // Handle errors (e.g., network failure, invalid movie ID)
    console.error('Error:', error.message);
  }
}

// Execute the main function
main();
