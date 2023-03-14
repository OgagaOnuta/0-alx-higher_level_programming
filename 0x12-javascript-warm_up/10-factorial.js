#!/usr/bin/node
// Computes and prints a factorial

const process = require('process');

function factorial (n) {
  if (isNaN(n) || (n < 0) || (n === 0) || (n === 1)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
