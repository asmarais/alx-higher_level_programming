#!/usr/bin/node

const args = process.argv.slice(2);
const value = parseInt(args[0]);

function fact (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(value));
