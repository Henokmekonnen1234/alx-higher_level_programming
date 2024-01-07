#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
console.log(list.map((number, index) => number * index));
