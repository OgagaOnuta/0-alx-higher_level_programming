#!/usr/bin/node
// Returns the reversed version of a list

exports.esrever = function (list) {
  const listCopy = [...list];
  const len = listCopy.length;
  const newList = [];
  let element;
  let i = 0;

  while (i < len) {
    i++;
    element = listCopy[len - i];
    newList.push(element);
  }

  return (newList);
};
