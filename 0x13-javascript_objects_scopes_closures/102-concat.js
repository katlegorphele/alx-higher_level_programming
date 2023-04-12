#!/usr/bin/node

const fs = require('fs');

// get the file paths from the command line arguments
const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

// read the contents of the source files
const contents1 = fs.readFileSync(file1, 'utf-8');
const contents2 = fs.readFileSync(file2, 'utf-8');

// concatenate the contents of the source files
const result = contents1 + contents2;

// write the result to the destination file
fs.writeFileSync(dest, result, 'utf-8');
