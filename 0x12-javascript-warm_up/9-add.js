#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);

if (args.length === 2) {
  const num1 = parseInt(args[0]);
  const num2 = parseInt(args[1]);

  if (!isNaN(num1) && !isNaN(num2)) {
    const result = add(num1, num2);
    console.log(result);
  } else {
    console.log(NaN);
  }
} else {
  console.log(NaN);
}
