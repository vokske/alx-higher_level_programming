#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}
	print() {
		let row = "X".repeat(this.width);
		for (let i = 0; i < this.height; i++) {
			console.log(row);
		}
	}
};
