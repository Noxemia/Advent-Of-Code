package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var bagMap map[string]bag

func main() {
	readData, err := ioutil.ReadFile("day7input.txt")
	if err != nil {
		fmt.Println("error on reading file", err)
		return
	}
	dataStrings := strings.Split(string(readData), "\n")
	fmt.Println(dataStrings)

	var allBags []bag
	for _, str := range dataStrings {
		allBags = append(allBags, bagBuilder(str))
	}
	bagMap = make(map[string]bag)
	for _, bag := range allBags {
		bagMap[bag.bagName] = bag
	}

	fmt.Println(bagRecurse(bagMap["shinygold"]))

}

func bagRecurse(b bag) int {
	if len(b.containedBags) == 0 {
		return 0
	}

	var tot int

	for i, elem := range b.containedBags {
		tot += b.numberOfBags[i] + b.numberOfBags[i]*bagRecurse(bagMap[elem])
	}

	return tot
}

type bag struct {
	bagName       string
	containedBags []string
	numberOfBags  []int
}

func bagBuilder(str string) bag {

	splitted := strings.Split(str, " ")
	name := splitted[0] + splitted[1]

	var contained []string
	var amount []int

	for i, value := range splitted[4:] {
		if value == "no" {
			break
		}
		if i%4 != 0 {
			continue
		}
		contained = append(contained, splitted[4:][i+1]+splitted[4:][i+2])
		number, _ := strconv.Atoi(splitted[4:][i])
		amount = append(amount, number)
	}
	return bag{name, contained, amount}
}
