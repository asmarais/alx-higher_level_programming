#!/usr/bin/node

const args = process.argv.slice(2);
const value = parseInt(args[0], 10);

if (!isNaN(value)) {
  for (let i = 1; i <= value; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
