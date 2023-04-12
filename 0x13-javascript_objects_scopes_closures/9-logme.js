#!/usr/bin/node
let count = 0; // create a count variable to keep track of the number of arguments printed

exports.logMe = function (item) {
  console.log(`${count}: ${item}`); // print the count and the new argument value
  count++; // increment the count variable
};
