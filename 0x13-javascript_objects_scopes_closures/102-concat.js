#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const filePath1 = fs.readFileSync(argv[2], 'utf-8').toString();
const filePath2 = fs.readFileSync(argv[3], 'utf-8').toString();
fs.writeFileSync(argv[4], filePath1 + filePath2);
