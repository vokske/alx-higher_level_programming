#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
		let row = c.repeat(this.size);
		for (let i = 0; i < this.size; i++) {
			console.log(row);
		}
	}
};
