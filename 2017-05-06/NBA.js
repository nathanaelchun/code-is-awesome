var nba = "NBA";
var a = "press anything and then enter";
var p = "Stephine Curry";
console.log(nba);

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question(a, (answer) => {
    console.log(p);
    rl.close();
});