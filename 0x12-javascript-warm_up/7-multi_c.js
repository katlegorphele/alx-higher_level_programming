#!/usr/bin/node

// Get the number of times text must be repeated from first argv arg
// and convert it to an int
const x = parseInt(process.argv[2]);

// Check if x is valid int. If valid print "C is fun" x times
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
