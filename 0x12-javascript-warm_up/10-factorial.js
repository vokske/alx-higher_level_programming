#!/usr/bin/node
function fact(num) {
if (num === 0) {
  return 1;
} return num * fact(num - 1);
}
const num1 = parseInt(process.argv[2]);
if (isNaN(num1)) {
  console.log('1');
}
console.log(fact(num1));
