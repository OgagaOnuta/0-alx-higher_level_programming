#!/usr/bin/node
// Prints a string a certain number of times

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
