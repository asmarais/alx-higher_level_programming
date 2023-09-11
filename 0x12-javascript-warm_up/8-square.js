#!/usr/bin/node

const args = process.argv.slice(2);
const value = parseInt(args[0], 10);
let s = '';

if (!isNaN(value)) {
  for (let i = 1; i <= value; i++) {
    s += 'X';
  }
  for (let i = 1; i <= value; i++) {
    console.log(s);
  }
} else {
  console.log('Missing size');
}
