#!/usr/bin/node

const bigNum = (x) => {
  if (process.argv.length <= 2) {
    console.log(0);
  } else {
    const x = process.argv.reduce((prev, next) => prev > next ? prev : next, 0);
    console.log(x);
  }
};

process.argv.splice(0, 2);
bigNum(process.argv);
