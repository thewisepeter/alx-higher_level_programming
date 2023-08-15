#!/usr/bin/node

function factorial (x) {
  if (x === 1) {
    return NaN;
  }
  return (factorial(x - 1) * x);
}
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log(1);
}
if (args.length === 1) {
  const x = parseInt(args[0]);
  if (!isNaN(x)) {
    console.log(factorial(x));
  }
}
