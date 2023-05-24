#!/usr/bin/node

const fs = require('fs');

function readFileContent (filePath) {
  // Read the file content using fs.readFile
  // with 'utf-8' encoding to interpret the content as text
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      // If an error occurred during reading, print the error object
      console.error(err);
    } else {
      // If reading is successful, print the file content
      console.log(data);
    }
  });
}

// Retrieve the file path from command line arguments
// The first argument (index 2) is the file path
const filePath = process.argv[2];

// Call the function to read and print the file content
readFileContent(filePath);
