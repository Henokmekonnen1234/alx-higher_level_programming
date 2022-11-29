#!/usr/bin/node

const process = require('process');
let args = process.argv[2];
if (parseInt(args)) {
  while (args > 0) {
    console.log('C is fun');
    args = args - 1;
}
} else {
  console.log('Missing number of occurrences');
}
