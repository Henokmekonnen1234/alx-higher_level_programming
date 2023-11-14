#!/usr/bin/node

if (Number(process.argv[2]) === NaN | Number(process.argv[2]) === undefined |
	Number(process.argv[2]) === 0 | Number(process.argv[2]) === 1) {
  console.log(1);
} else {
  let number = 1;
  for (let i = 1; i <= Number.parseInt(process.argv[2]); i++){
    number *= i;
  }
  console.log(number);
}
