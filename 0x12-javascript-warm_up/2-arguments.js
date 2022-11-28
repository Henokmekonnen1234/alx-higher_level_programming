#!/usr/bin/node
process = require('process');
const args= process.argv
if (args[2]) {
console.log('Arguments found',args[2]);
} else {
console.log('No argument');
}
