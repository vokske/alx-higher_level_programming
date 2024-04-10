#!/usr/bin/node
const arg1 = process.argv[2];
const myStr = 'C is fun';
const num = parseInt(arg1);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log(myStr);
  }
} else {
  console.log('Missing number of occurrences');
}
