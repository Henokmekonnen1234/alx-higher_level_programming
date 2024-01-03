#!/usr/bin/node

const number = function (x) {
  if (isNaN(x) || x === 1 || x === 0) {
    return 1;
  } else {
    return x * (number(x - 1));
  }
};

console.log(number(Number.parseInt(process.argv[2])));
