#!/usr/bin/node

const { argv } = require('node:process');
let length = 0;
argv.forEach((value, index) => { length += 1; });
if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No Argument');
}
