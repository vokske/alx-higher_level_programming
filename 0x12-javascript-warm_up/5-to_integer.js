#!/usr/bin/node
const arg1 = process.argv[2];
const num = parseInt(arg1);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
