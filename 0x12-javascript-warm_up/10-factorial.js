#!/usr/bin/node
function fact (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * fact(num - 1);
}
const num1 = parseInt(process.argv[2]);
console.log(fact(num1));
