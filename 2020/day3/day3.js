const fs = require('fs')

const rl = require('readline')

const interface = rl.createInterface({
    input: fs.createReadStream('./day3input.txt')
})

function readLines(modx, mody) {
    let posx = 0;
    let posy = 0;
    let treeCounter = 0;
    let xes = []
    let yes = []
    return readPromise = new Promise((res, rej) => {

        let posx = 0;
        let posy = 0;
        let treeCounter = 0;
        interface.on("line", (line) => {
            console.log(posx)
            if((posy % mody) == 0){
                if(line.split('')[posx] == '#') treeCounter++
                posx = posx + modx
                if(posx >= line.length) posx = posx - line.length
                
            }
            posy++
            
            
        }).on("close", () => {
//console.log(xes.map((x, i) => {return  `${x} - ${yes[i]}`}))
           res(treeCounter)
        })
    
    })
}

async function main(){
    //let f = readLines(1,1)
    let s = readLines(3,1)
    //let t = readLines(5,1)
   // let fo = readLines(7,1)
    //let fi = readLines(1,2)

    return Promise.all([f, s, t, fo, fi])
}
main().then(data => {console.log(data.reduce((acc, value) => acc *= value))})
//main().then(data => {console.log(data)})

async function test(){
     let fo = await readLines(1,2)
     console.log(fo)
}
//test()
let lmao = [1,2,3]
