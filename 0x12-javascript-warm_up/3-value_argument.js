#!/usr/bin/node

const { argv } = require('node:process');
let length = 0;
argv.forEach((value, index) => { length += 1; });
if (length <= 2) {
  console.log('No Argument');
} else {
  console.log(argv[2]);
}
