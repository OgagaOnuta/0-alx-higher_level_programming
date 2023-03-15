#!/usr/bin/node
// Prints the number of arguments already printed
// and the new argument value

exports.logMe = (function (item) {
  let numArg = 0;
  return (item) => {
    console.log(numArg + ': ' + item);
    return (numArg++);
  };
})();
