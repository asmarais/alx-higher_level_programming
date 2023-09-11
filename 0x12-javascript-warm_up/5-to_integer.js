#!/usr/bin/node

const args = process.argv.slice(2);
const value = parseInt(args[0], 10);

if (!isNaN(value)) {
  console.log('My number: ' + parseInt(value, 10));
} else {
  console.log('Not a number');
}
