#!/usr/bin/node

process.argv.sort();
if (process.argv.length >= 4) {
  console.log(Number.parseInt(process.argv[process.argv.length - 2]));
} else {
  console.log(0);
}
