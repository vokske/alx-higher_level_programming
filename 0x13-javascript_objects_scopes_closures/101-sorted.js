#!/usr/bin/node
const dict = require('./101-data').dict;

const newArray = Object.entries(dict);
const newKeys = newArray.map(subarray => subarray[1]);
const newValues = newArray.map(subarray => subarray[0]);
let newDict = {};
newKeys.forEach((key, index) => {
	const value = newValues[index];
	if (!newDict[key]) {
		newDict[key] = [];
	}
	newDict[key].push(value);
});
console.log(newDict);
