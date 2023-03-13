#!/usr/bin/node
// Converts an argument to an integer

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  const convInt = parseInt(process.argv[2]);
  console.log('My number: ' + convInt);
}
