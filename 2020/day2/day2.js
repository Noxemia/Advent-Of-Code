const fs = require('fs')
const readline = require('readline')

const readInterface = readline.createInterface({
    input: fs.createReadStream('./day2input.txt')
})


function part1(){
    let noCorrect = 0;
    return new Promise((res, err) => {
        readInterface.on('line', (line) => {
            const numbers = line.match(/\d/g)
            const lineLoc = line.match(/-/).index

            let letter = line.match(/[a-z]/)[0]
            let regex = new RegExp(letter, 'g')
            let noLetters = line.match(regex).length-1
            let fn = 0;
            let sn = 0;
            if(numbers.length == 4){
                fn = parseInt(numbers[0] + numbers[1])
                sn = parseInt(numbers[2] + numbers[3])
            }else if(numbers.length == 2){
                fn = parseInt(numbers[0])
                sn = parseInt(numbers[1])
            }else if(lineLoc == 1){
                fn = parseInt(numbers[0])
                sn = parseInt(numbers[1] + numbers[2])
            }else{
                fn = parseInt(numbers[0] + numbers[1])
                sn = parseInt(numbers[2])
            }
            if(fn <= noLetters && noLetters <= sn) noCorrect++
            
        }).on("close", () => {
            res(noCorrect)
        })

    })
}

function part2(){
    let noCorrect = 0;
    return new Promise((res, err) => {
        readInterface.on('line', (line) => {
            const letter = line.match(/[a-z]/)[0]
            const colonIndex = line.match(/:/).index
            const textOnly = line.slice(colonIndex+1)

            const numbers = line.match(/\d/g)
            const lineLoc = line.match(/-/).index
            let fn = 0;
            let sn = 0;
            if(numbers.length == 4){
                fn = parseInt(numbers[0] + numbers[1])
                sn = parseInt(numbers[2] + numbers[3])
            }else if(numbers.length == 2){
                fn = parseInt(numbers[0])
                sn = parseInt(numbers[1])
            }else if(lineLoc == 1){
                fn = parseInt(numbers[0])
                sn = parseInt(numbers[1] + numbers[2])
            }else{
                fn = parseInt(numbers[0] + numbers[1])
                sn = parseInt(numbers[2])
            }

            let firstStatement = (textOnly[fn] == letter)
            let secondStatement = (textOnly[sn] == letter)

            if((firstStatement || secondStatement) && !(firstStatement && secondStatement)) noCorrect++
            
            
        }).on("close", () => {
            res(noCorrect)
        })

    })
}


//part1().then(console.log)
part2().then(console.log)
