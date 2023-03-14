#!/usr/bin/node
// Creates a class that inherits from another class

const SuperSquare = require('./5-square');

module.exports = class Square extends SuperSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let str = '';
    let i = 0;
    let j = 0;

    while (i < this.height) {
      while (j < this.width) {
        str += c;
        j++;
      }
      console.log(str);
      i++;
    }
  }
};
