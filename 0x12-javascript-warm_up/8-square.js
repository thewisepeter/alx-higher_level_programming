#!/usr/bin/node

const square = 'X';
const args = process.argv.slice(2);
const x = parseInt(args[0]);
if (!isNaN(x)) {
  for (let i = 0; i <= x; i++) {
    let row = '';
    for (let j = 0; j <= x; j++) {
      row += square;
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
