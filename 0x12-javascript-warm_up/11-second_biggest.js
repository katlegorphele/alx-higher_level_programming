#!/usr/bin/node

// Parse the integer arguments from the command line and convert them to numbers
const args = process.argv.slice(2).map(Number);

// If no arguments were passed or there's only one argument, print 0
if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  // Sort the arguments in descending order
  const sortedArgs = args.sort((a, b) => b - a);

  // Find the second biggest integer in the sorted arguments
  const secondBiggest = sortedArgs[1];

  // Print the second biggest integer
  console.log(secondBiggest);
}
