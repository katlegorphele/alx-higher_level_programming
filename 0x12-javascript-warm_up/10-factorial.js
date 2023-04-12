#!/usr/bin/node

// Define the recursive factorial function
function factorial(n) {
    // Base case: factorial of 0 or 1 is 1
    if (n === 0 || n === 1) {
      return 1;
    }
    // Recursive case: factorial of n is n times the factorial of n-1
    else {
      return n * factorial(n-1);
    }
  }
  
  // Parse the integer argument from the command line and convert it to a number
  const arg = Number(process.argv[2]);
  
  // Check if the argument is not a number or NaN
  if (isNaN(arg)) {
    console.log("1");
  } else {
    // Compute the factorial using the factorial function and print the result
    console.log(factorial(arg));
  }
  