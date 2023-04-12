#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0, rows; i < size; i++) {
    rows = '';
    for (let j = 0; j < size; j++) {
      rows += 'X';
    }
    console.log(rows);
  }
}
