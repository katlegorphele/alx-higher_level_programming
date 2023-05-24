#!/usr/bin/node

const request = require('request');

// Get url from argv
const url = process.argv[2];

// Run GET request to url
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
