#!/usr/bin/node
// Executes a function a certain number of times

exports.callMeMoby = function (x, theFunction) {
  while (x) {
    theFunction();
    x--;
  }
};
