#!/usr/bin/node

const { argv } = require('node:process');
const args = argv.slice(2);
if (args.length > 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
