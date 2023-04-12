#!/usr/bin/node

const dict = require('./101-data');

const occurrences = {};
for (const key in dict) {
  const value = dict[key];
  if (value in occurrences) {
    occurrences[value].push(key);
  } else {
    occurrences[value] = [key];
  }
}

console.log(occurrences);
