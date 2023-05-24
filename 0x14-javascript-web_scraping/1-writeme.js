#!/usr/bin/node

const fs = require('fs');

function writeFileContent (filePath, content) {
  // Write content to file us fs.writeFile
  // with 'utf-8' encoding to intepret content as text
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      // If error occurs during write, print error obj
      console.log(err);
    } else {
      // If writing succeeds print message
      console.log('File written successfully');
    }
  });
}

// Retrieve path and commands as argv

const filePath = process.argv[2];
const content = process.argv[3];

// Call function to write
writeFileContent(filePath, content);
