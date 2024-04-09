#!/usr/bin/node
const argsLen = process.args.length;
if (argsLen === 2){
	console.log('No Argument');
} else if(argsLen === 3){
	console.log('Argument found');
} else{
	console.log('Arguments found');
}
