#!/usr/bin/node

const process = require('process');
const args = [];

if (process.argv.length <= 2) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    args.push(parseInt(process.argv[i]));
  }
  args.sort(function (a, b) { return a - b; });
  console.log(args[args.length - 2]);
}
