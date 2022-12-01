package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func main() {
	readData, err := ioutil.ReadFile("day10input.txt")
	if err != nil {
		fmt.Println("error on reading file", err)
		return
	}
	dataStrings := strings.Split(string(readData), "\n")

	var dataNumeric []int
	for _, l := range dataStrings {
		str := parseOutNum(l)
		conv, err := strconv.Atoi(str)
		if err != nil {
			fmt.Println("error in parsing string", err)
			return
		}
		dataNumeric = append(dataNumeric, conv)
	}
	sort.Ints(dataNumeric)

	/// Part one
	diffThree := 1

	for i, n := range dataNumeric {
		if i == len(dataNumeric)-1 {
			break
		}
		if dataNumeric[i+1]-n == 3 {
			diffThree++
		}
	}

	//fmt.Println((len(dataNumeric) - diffThree) * diffThree)

	/// Part Two

	for i := range cache {
		cache[i] = 0
	}

	fmt.Println(partTwoRecurse(dataNumeric))
	//fmt.Println(cache)

}

var cache [1000]int

func partTwoRecurse(data []int) int {
	res := 0
	if len(data) == 1 {
		return 1
	}
	if cache[data[0]] != 0 {
		return cache[data[0]]
	}
	for i, n := range data[1:] {
		if n-data[0] > 3 {
			break
		}
		res += partTwoRecurse(data[i+1:])
		cache[data[0]] = res
	}
	return res
}

func parseOutNum(str string) string {
	/*if len(str) == 2 {
		return str[0:1]
	}
	if len(str) == 3 {
		return str[0:2]
	}
	if len(str) == 4 {
		return str[0:3]
	}

	for _, i := range str {

	}*/

	return str[0 : len(str)-1]
}
