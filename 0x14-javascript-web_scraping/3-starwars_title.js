#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Retrieve the movie ID from command line arguments
const id = process.argv[2];

// Make a GET request to the Star Wars API endpoint for the specified movie ID
request('http://swapi.co/api/films/' + id + '/', function (error, response, body) {
  // Check if there is no error
  if (error == null) {
    // Parse the response body as JSON
    const json = JSON.parse(body);

    // Print the title of the movie
    console.log(json.title);
  }
});
