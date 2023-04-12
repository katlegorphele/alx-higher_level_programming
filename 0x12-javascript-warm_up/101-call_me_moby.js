#!/usr/bin/node

function executeXTimes(x, theFunction) {
    for (let i = 0; i < x; i++) {
      theFunction();
    }
}
  
  // Example usage:
  function printHello() {
    console.log('Hello!');
}
  
executeXTimes(5, printHello); // Output: Hello! Hello! Hello! Hello! Hello!
  