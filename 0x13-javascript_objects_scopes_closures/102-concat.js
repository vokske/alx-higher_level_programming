#!/usr/bin/node
const fs = require('fs');

const path1 = process.argv[2];
const path2 = process.argv[3];
const destinationFile = process.argv[4];

const content1 = fs.readFileSync(path1);
const content2 = fs.readFileSync(path2);
const concatContent = content1 + content2;
fs.writeFileSync(destinationFile, concatContent);
