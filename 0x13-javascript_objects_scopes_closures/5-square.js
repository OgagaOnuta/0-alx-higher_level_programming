#!/usr/bin/node
// Creates a class that inherits from another class

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
