#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0; // Initialize count to 0
  // Loop through each element in the list
  for (const element of list) {
    // If the current element is equal to the search element
    if (element === searchElement) {
      count++; // Increment the count
    }
  }
  return count; // Return the final count
};
