#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c !== undefined || c !== null || !isNaN(c)) {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
