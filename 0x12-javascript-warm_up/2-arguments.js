#!/usr/bin/node
// Prints a message depending on the number of arguments passed

const process = require('process');

if (process.argv.length > 3) {
  console.log('Arguments found');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
