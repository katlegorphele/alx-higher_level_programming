#!/usr/bin/node

// Define the add function that takes two parameters and returns their sum
function add(a, b) {
    return a + b;
  }
  
  // Parse the two integer arguments from the command line and convert them to numbers
  const arg1 = Number(process.argv[2]);
  const arg2 = Number(process.argv[3]);
  
  // Check if either argument is not a number
  if (isNaN(arg1) || isNaN(arg2)) {
    console.log("Invalid arguments");
  } else {
    // Call the add function with the parsed arguments and print the result
    console.log(add(arg1, arg2));
  }