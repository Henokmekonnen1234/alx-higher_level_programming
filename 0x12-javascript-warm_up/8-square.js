#!/usr/bin/node

if (Number(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
