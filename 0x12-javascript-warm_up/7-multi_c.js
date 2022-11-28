#!/usr/bin/node

const process = require('process');
const args = process.argv[2]
while (args > 0) {
  console.log('C is fun');
  args--;
}
