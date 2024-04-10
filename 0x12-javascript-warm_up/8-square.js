#!/usr/bin/node
const sqSize = process.argv[2];
const sqChar = 'X';
const num = parseInt(sqSize);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += sqChar;
    }
    console.log(row);
  }
}
