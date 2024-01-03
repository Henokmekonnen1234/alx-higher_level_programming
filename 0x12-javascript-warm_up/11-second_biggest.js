#!/usr/bin/node

const bigNum = (x) => {
  if (process.argv.length <= 2) {
    console.log(0);
  } else {
    console.log(process.argv[process.argv.length - 1]);
  }
};

process.argv.splice(0, 2);
bigNum(process.argv.sort());
