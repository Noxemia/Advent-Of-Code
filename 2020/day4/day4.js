const fs = require('fs')
const rl = require('readline')

const readingInterface = rl.createInterface({
    input: fs.createReadStream('day4input.txt')
})

function part1(){
    let all = []
    let current = ""

    return new Promise((res, err) => {
        readingInterface.on("line", (line) => {
            current += line;
            if(line == ""){
                all.push(current)
                current = ""
            }
        }).on("close", () => {
            res(all)
        })
    })

}

part1().then(data => {
    let noCorrects = 0;
    let corrects = [];
    const regex = /(byr:(19[2-9][0-9]|200[0-2])|iyr:(201[0-9]|2020)|eyr:(202[0-9]|2030)|hgt:((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in))|hcl:#[a-z0-9]{6}|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:[0-9]{9})/gm
    return new Promise((res, err) => {
        data.forEach((element, index) => {
            if(element.match(regex)){
                if(element.match(regex).length == 7) {noCorrects++;corrects.push(element)}
            } 
            
            if(index == data.length-1) {res(noCorrects); console.log(corrects)}
        });

    })
}).then(console.log)