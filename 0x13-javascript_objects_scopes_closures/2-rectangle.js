#!/usr/bin/node

// Class Definition
class Rectangle {
  // Create constructor
  constructor (w, h) {
    // create empty object if w/h < 0 or not a num
    // Asign width and height vals to instance properties
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
