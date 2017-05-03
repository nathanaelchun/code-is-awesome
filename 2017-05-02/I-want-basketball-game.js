var a = "Michael Jordan";
var b = "Kevin Durant";

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Who is the best basketball player, " + a + " or " + b+"?", (answer) => {
    if(answer==a)
    {
      console.log("Right!!!");
    }
    if(answer==b)
    {
        console.log("Wrong!!!");
    }
    rl.close();
});
