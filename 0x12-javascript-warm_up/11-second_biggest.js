#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

const process = require('process');

const len = process.argv.length;

// Function to create an array from the list of arguments
function createArray () {
  const myArray = [];
  let i = 2;

  while (i < len) {
    myArray.push(parseInt(process.argv[i]));
    i++;
  }

  return (myArray);
}

// Function to search for the biggest element in the array
function searchBiggest (givenArray) {
  const givenLength = givenArray.length;
  let i = 2;
  let bigger;

  if (givenArray[0] > givenArray[1]) {
    bigger = givenArray[0]; // First element is bigger
  } else {
    bigger = givenArray[1]; // Second element is bigger
  }

  while (i < givenLength) {
    if (bigger < givenArray[i]) {
      bigger = givenArray[i]; // Next element is bigger
    }
    i++;
  }

  return (bigger);
}

if ((len === 2) || (len === 3)) {
  console.log(0);
} else {
  const myArray = createArray(); // Create the array
  const big = searchBiggest(myArray); // Search for the biggest element
  const myIndex = myArray.indexOf(big); // Get the index of the biggest element
  myArray.splice(myIndex, 1); // Remove the biggest element from the array
  const secondBiggest = searchBiggest(myArray); // Search for the current biggest element
  console.log(secondBiggest); // Print it to the console
}
