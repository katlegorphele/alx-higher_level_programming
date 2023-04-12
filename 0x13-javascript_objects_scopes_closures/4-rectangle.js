#!/usr/bin/node

class Rectangle {
  // Constructor function
  constructor (w, h) {
    // Check if width and height are valid positive integers
    if (w > 0 && h > 0) {
      // Set the width and height of the rectangle
      this.width = w;
      this.height = h;
    } else {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      return {};
    }
  }

  // Print method to print the rectangle with X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Rotate method to exchange the width and height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Double method to double the width and height of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
