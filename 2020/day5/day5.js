const fs = require('fs')
const rl = require('readline')

const readingInterface = rl.createInterface({
    input: fs.createReadStream('day5input.txt')
})

function part1(){

    return new Promise((res, err) => {

        let ans = []

        readingInterface.on("line", line => {

            const seven = line.slice(0,7)
            const three = line.slice(7)
            let lo = 0;
            let hi = 127;
            seven.split('').forEach(l => {
                if(l == "F") hi = Math.floor(hi - ((hi-lo)/2))
                if(l == "B") lo = Math.ceil(lo + ((hi-lo)/2))
            })

            let lo2 = 0;
            let hi2 = 7;
            three.split('').forEach(l => {
                if(l == "L") hi2 = Math.floor(hi2 - ((hi2-lo2)/2))
                if(l == "R") lo2 = Math.ceil(lo2 + ((hi2-lo2)/2))
            })

            ans.push(lo*8+lo2)
        }).on('close', ()=> {
            res(ans)
        })

    })


}

part1().then(data => {
    console.log(Math.max(...data))
})
// Part2
part1().then(data => {
    data.sort().forEach((elem, index) => {

        if(data[index+1] - elem == 2){
            console.log(elem+1)
        }
    })
})