#!/usr/bin/node
const dict = require('./101-data').dict;
const dictionary = {};
const prevValue = [];
for (const key in dict) {
  if (!prevValue.includes(dict[key])) {
    prevValue.push(dict[key]);
    dictionary[dict[key]] = [];
  }
  dictionary[dict[key]].push(key);
}
console.log(dictionary);
