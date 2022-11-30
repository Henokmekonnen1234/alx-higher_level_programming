#!/usr/bin/node

const process = require('process');
const args = process.argv;

for (let i = 2; i < args.length; i++){
  if (args[i] > args[i + 1]) {
    const temp = a[i];
    a[i] = a[i + 1];
    a[i + 1] = temp;
}
}
console.log(args[2...])
