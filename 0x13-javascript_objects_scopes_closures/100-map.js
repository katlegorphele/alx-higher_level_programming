#!/usr/bin/node
const list = require('./100-data').list;

console.log('Original list:', list);

const newList = list.map((value, index) => value * index);

console.log('New list:', newList);
