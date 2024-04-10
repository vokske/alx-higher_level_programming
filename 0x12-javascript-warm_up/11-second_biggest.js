#!/usr/bin/node
const myArray = [];
const argsLen = process.argv.length;

if (argsLen === 2 || argsLen === 3) {
  console.log('0');
} else {
  for (let i = 2; i <= argsLen; i++) {
    myArray.push(parseInt(process.argv[i]));
  }myArray.sort((a, b) => b - a);
  console.log(myArray[1]);
}
