#!/usr/bin/node
// Creates a class that inherits from another class

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
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
