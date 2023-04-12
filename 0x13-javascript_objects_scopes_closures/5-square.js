#!/usr/bin/node
// Rectangle class definition
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if width or height is 0 or negative
      return {};
    }
  }

  // Method to print the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Method to exchange the width and the height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Method to double the width and the height of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

// Square class definition that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of Rectangle using super() with size as both arguments
    super(size, size);
  }
}

module.exports = Square;
