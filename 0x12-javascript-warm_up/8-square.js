#!/usr/bin/node
// Prints a square

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);

  function str () {
    let str = '';
    let i = 0;

    while (i < x) {
      str += 'X';
      i++;
    }

    return (str);
  }

  let i = 0;
  while (i < x) {
    console.log(str());
    i++;
  }
}
