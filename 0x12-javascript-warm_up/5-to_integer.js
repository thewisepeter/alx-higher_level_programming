#!/usr/bin/node

const args = process.argv.slice(2);
const firstArgAsInt = parseInt(args[0]);

if (!isNaN(firstArgAsInt)) {
  console.log(`My number: ${firstArgAsInt}`);
} else {
  console.log('Not a number');
}
