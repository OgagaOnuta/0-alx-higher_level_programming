#!/usr/bin/node
// Create an class that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const wid = () => {
      let str = '';
      let i = 0;

      while (i < this.width) {
        str += 'X';
        i++;
      }

      return (str);
    };

    let i = 0;
    while (i < this.height) {
      console.log(wid());
      i++;
    }
  }
};
