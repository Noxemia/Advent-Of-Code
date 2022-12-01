const fs = require('fs')
const rl = require('readline')

const readInterface = rl.createInterface({
    input: fs.createReadStream('day6input.txt')
})


function part1(){
    let all = []
    let current = ""

    return new Promise((res, err) => {
        readInterface.on("line", (line) => {
            current += line;
            if(line == ""){
                all.push(current)
                current = ""
            }
        }).on("close", () => {
            all.push(current)
            res(all)
        })
    })

}

part1().then(data => {
    let list = []
    data.forEach(element => {
      list.push(element.split('').sort())
    });
    let counts = []
    let current = ""
    let counter = 0;
    list.forEach(list => {
        list.forEach(char => {
            if(!(char == current)){
                current = char;
                counter++
            }
        })
        counts.push(counter)
        current = "";
        counter = 0;
    })
    console.log(counts.reduce((acc, num) => acc+=num))

})


function part2(){
    let all = []
    let current = []

    return new Promise((res, err) => {
        readInterface.on("line", (line) => {
            if(line != "") current.push(line.split(''));
            if(line == ""){
                all.push(current)
                current = []
            }
        }).on("close", () => {
            all.push(current)
            res(all)
        })
    })

}

part2().then(data => {
    let counts = []
    data.forEach(smth => {
    let reference = smth[0]
    
    //console.log(reference)
    let count = 0;
   reference.forEach(ref => {
       let ans = true;
       

        for(let i = 1; i < smth.length; i++){
            console.log(!smth[i].includes(ref))
            if(!smth[i].includes(ref)) ans = false
        }
        if(ans) count++
       
   })
   counts.push(count)
})
   
console.log(counts.reduce((acc, num) => acc+=num))
})