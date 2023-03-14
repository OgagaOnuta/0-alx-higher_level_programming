#!/usr/bin/node
// Prints the addition of 2 integers

const process = require('process');

function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  return (a + b);
}

console.log(add());
