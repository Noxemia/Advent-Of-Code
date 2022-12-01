const fs = require('fs')
const rl = require('readline')

const ri = rl.createInterface({
    input: fs.createReadStream('day7input.txt')
})


function part1(){
    return new Promise((res, err) => {
        let data = []
        ri.on('line', line => {
            let bagColor = ""
            let innerBags = []
            let words = line.split(" ")
            bagColor = words[0] + words[1]
            words = words.splice(3, words.length)
            words.forEach((elem, index) => {
                if(elem == "bags," || elem == "bags." || elem == "bag," || elem == "bag."){
                    if(words[index-2] != "no")  {
                        innerBags.push(words[index-2] + words[index-1])
                    }
                }
            })

            data.push([bagColor, innerBags])


        }).on('close', () => {

            res(data)
        })
    })
}

part1().then(data => {
    return
    let promises = []
    data.forEach(elem => {
        promises.push(part1Recurser(data, elem[0]))
    })

    Promise.all(promises).then(data2 => {
        let counter = 0;
        data2.forEach(elem => {
            if(elem == true ) counter ++
        })
        console.log(counter)
    })
})


async function part1Recurser( data, bag){
    return new Promise((res, err) => {
        data.forEach(elem => {
            // finds the bag element in the dataset
            if(elem[0] == bag){
                
                // if the element includes shiny gold return true
                if(elem[1].includes("shinygold")){
                    res(true)
                }else if(elem[1].length == 0) 
                // incase no shinygold was found and there were no bags inside, return false
                {res(false)
                }else{
                    // if there are bags inside recurse on these bags
                    let recursePromises = []
                    elem[1].forEach(elem2 => {
                        recursePromises.push(part1Recurser(data, elem2))
                    })
                    Promise.all(recursePromises).then(data2 => {
                        // if a bag underneath in the tree would contain one shiny it means that the 
                        // toplevel bag can contain it, therefore return true if we find a single true
                        data2.includes(true) ? res(true) : res(false)
                    }
                        
                    )
                }
            }
            
        })

    })
}

function part2(){
    return new Promise((res, err) => {
        let data = []
        ri.on('line', line => {
            let bagColor = ""
            let innerBags = []
            let words = line.split(" ")
            bagColor = words[0] + words[1]
            words = words.splice(3, words.length)
            words.forEach((elem, index) => {
                if(elem == "bags," || elem == "bags." || elem == "bag," || elem == "bag."){
                    if(words[index-2] != "no")  {
                        innerBags.push([words[index-2] + words[index-1], parseInt(words[index-3])])
                    }
                }
            })

            data.push([bagColor, innerBags])

            
        }).on('close', () => {

            res(data)
        })
    })
}

part2().then(data => {
    // find the gold bag as starting node, for loop to be able to break out of it
    for(let i = 0; i < data.length; i++){
        if(data[i][0] == "shinygold") {
            part2Recurser(data, i).then(console.log)
            break;
        }
    }

})

async function part2Recurser(data, dataIndex){
    let node = data[dataIndex]
    return new Promise((res, err) => {
        if(node[1].length == 0) {res(0)}
        let recursePromises = []
        let recureMultipliers = []
        node[1].forEach(elem => {

            for(let i = 0; i < data.length; i++){
                if(data[i][0] == elem[0]) {
                    console.log(elem)
                    recursePromises.push(elem[1])
                    recursePromises.push(part2Recurser(data, i))
                    break;
                }
            }
        })
        
        Promise.all(recursePromises).then( result => {
            res(result.forEach((elem2, index) => {elem2 * recureMultipliers[index]}).reduce((acc, elem3) => acc+=elem3) + recureMultipliers.reduce((acc, elem4) => acc+=elem4))
        })
        
    })
}