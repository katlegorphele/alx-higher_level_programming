#!/usr/bin/node

function incrementAndCall(number, theFunction) {
  number++;
  theFunction(number);
}

// Example usage:
function printNumber(number) {
  console.log(number);
}

incrementAndCall(5, printNumber); // Output: 6
