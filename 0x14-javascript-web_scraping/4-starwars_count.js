#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from command line arguments
// The first argument (index 2) is the API URL
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const characterId = 18;

// Perform a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    try {
      // Parse the response body as JSON
      const filmsData = JSON.parse(body);

      // Filter the films where Wedge Antilles is present
      const filmsWithWedge = filmsData.results.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );

      // Print the number of films where Wedge Antilles is present
      console.log(`${filmsWithWedge.length}`);
    } catch (error) {
      console.error(`Error parsing JSON: ${error}`);
    }
  }
});
