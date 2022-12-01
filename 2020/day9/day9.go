package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	readData, err := ioutil.ReadFile("day9input.txt")
	if err != nil {
		fmt.Println("error on reading file", err)
		return
	}
	dataStrings := strings.Split(string(readData), "\n")
	var parsedData []int

	for _, str := range dataStrings {
		parsedData = append(parsedData, parseNumber(str))
	}
	//fmt.Println(parsedData)

	////// Part 1
	readNumbers := 25

	for {
		found := false
		consider := parsedData[readNumbers]
		for _, i := range parsedData[readNumbers-25 : readNumbers-1] {
			for _, j := range parsedData[readNumbers-24 : readNumbers] {
				if i+j == consider && i != j {
					fmt.Println(i, j, i+j, consider)
					found = true
					break
				}
			}
		}

		if !found {
			fmt.Println(consider)
			break
		}
		readNumbers++
	}

	///// Part 2 - 27911108, is row 510 elem in input

	index := 508 // 0 indexed first elem after 27911108

	for {
		var acc int
		var numbers []int

		for i := range parsedData[0 : index+1] {
			acc += parsedData[index-i]
			numbers = append(numbers, parsedData[index-i])
			if acc == 27911108 {
				fmt.Println(numbers)
				return
			}
			if acc > 27911108 {
				break
			}
		}
		index--

	}

}

func parseNumber(str string) int {
	var number int

	numberxd, _ := strconv.Atoi(string(str[0 : len(str)-1]))
	number = numberxd

	return number
}
