#!/usr/bin/node
const process = require('process');
const args = process.argv[2];
let value = '';
if (parseInt(args)) {
  for (let i = 1; i <= args; i++) {
    for (let j = 1; j <= args; j++) {
     value += 'X';
     if (j == args) {
      console.log(value);
}}
    value = '';
}} else {
  console.log('Missing size');
}
