#!/usr/bin/node
// Define a function named 'esrever' that takes a list as input and returns the reversed list
exports.esrever = function (list) {
  // Create a new empty list to store the reversed elements
  const reversedList = [];

  // Iterate through each element of the input list starting from the last element
  for (let i = list.length - 1; i >= 0; i--) {
    // Add the current element to the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
