#!/usr/bin/node

// Destruct first element in 'process.argv' array
const [, , arg1] = process.argv;

// Convert arg1 to int using parseInt(...)
const num = parseInt(arg1);

// Check whether num is valid int using Number.IsInteger(...)
if (Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
