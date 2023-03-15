#!/usr/bin/node
// Returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  const listCopy = [...list];
  let len = listCopy.length;
  const occur = [];
  let seen;
  let seenIndex;
  let element;
  let i = 0;

  while (i < len) {
    if (listCopy[i] === searchElement) { // Seen occurrence
      seen = listCopy[i];
      seenIndex = listCopy.indexOf(seen); // Get the index of the occurrence
      element = listCopy.splice(seenIndex, 1);
      occur.push(element); // Remove element from the list
      i = 0;
      len--;
    }
    i++;
  }

  const num = occur.length;
  return (num);
};
