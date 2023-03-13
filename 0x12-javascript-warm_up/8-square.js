#!/usr/bin/node
// Prints a square

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let str = '';
  let i = 0;
  let j = 0;

  while (i < x) {
    while (j < x) {
      str += 'X';
      j++;
    }
    console.log(str);
    i++;
  }
}
