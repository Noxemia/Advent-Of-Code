const fs = require('fs')
const rl = require('readline')

const ri = rl.createInterface({
    input: fs.createReadStream('day7input.txt')
})


function part1(){
    return new Promise((res, err) => {
        let data = []
        ri.on('line', line => {
            let parsed = line

            data.push(parsed)
        }).on('close', () => {

            res(data)
        })
    })
}

part1().then(console.log)


function part2(){
    return new Promise((res, err) => {
        let data = []
        ri.on('line', line => {
            let parsed = line

            data.push(parsed)
        }).on('close', () => {

            res(data)
        })
    })
}

part2().then(console.log)