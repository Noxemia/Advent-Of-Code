const fs = require('fs')
const readline = require('readline');

const readInterface = readline.createInterface({
    input: fs.createReadStream('./day1input.txt')
});
let data = []
readInterface.on('line', (line) => {
   data.push(parseInt(line))   
});

setTimeout(() => {part1();part2()}, 1000)
function part1(){
    for(let i = 0; i < data.length; i++){
        for(let j = i+1; j < data.length; j++){
            if(data[i] + data[j] == 2020){console.log("found 1", data[i], data[j])}
        }
    }
}


function part2(){
    for(let i = 0; i < data.length; i++){
        for(let j = i+1; j < data.length; j++){
            for(let k = j+1; k < data.length; k++){
                if(data[i] + data[j] + data[k] == 2020){console.log("found 2", data[i], data[j], data[k])}
            }
        }
    }
}