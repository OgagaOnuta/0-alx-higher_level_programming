#!/usr/bin/node
// Executes a function a certain number of times

module.exports.callMeMoby = function (x, theFunction) {
  while (x) {
    theFunction();
    x--;
  }
};
