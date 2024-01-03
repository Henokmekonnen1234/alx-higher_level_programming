#!/usr/bin/node

const bigNum = (x) => {
  if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const x = process.argv.reduce((prev, next) => prev > next ? prev : next, 0);
    console.log(x);
  }
};

bigNum(process.argv);
