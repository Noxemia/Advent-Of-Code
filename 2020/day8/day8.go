package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	readData, err := ioutil.ReadFile("day8input.txt")
	if err != nil {
		fmt.Println("error on reading file", err)
		return
	}
	dataStrings := strings.Split(string(readData), "\n")

	for i := range visited {
		visited[i] = false
	}
	acc = 0
	//part 1
	fmt.Println(instruction(dataStrings, 0))

	for i, insts := range dataStrings {
		var copy []string

		for _, elem := range dataStrings {
			copy = append(copy, elem)
		}

		if string(insts[0]) == "j" {
			newConfig := "n" + insts[1:]
			copy[i] = string(newConfig)
			instConfigs = append(instConfigs, copy)
		}
	}

	for _, inst := range instConfigs {
		for i := range visited {
			visited[i] = false
		}
		acc = 0
		fmt.Println(instruction(inst, 0))
	}

}

var instConfigs [][]string
var visited [1000]bool
var acc int

func instruction(instructions []string, pc int) int {
	if visited[pc] == true {
		return 0
	}
	visited[pc] = true

	if string(instructions[pc][0]) == "n" {
		return instruction(instructions, pc+1)
	} else if string(instructions[pc][0]) == "a" {
		number, sign := parseNumberAndSign(instructions[pc])
		if sign == "-" {
			acc -= number
		}
		if sign == "+" {
			acc += number
		}
		return instruction(instructions, pc+1)
	} else if string(instructions[pc][0]) == "e" {
		fmt.Println(string(instructions[pc][0]))
		fmt.Println("Exited", acc)
		return acc
	} else {
		number, sign := parseNumberAndSign(instructions[pc])
		if sign == "-" {
			return instruction(instructions, pc-number)
		}
		if sign == "+" {
			return instruction(instructions, pc+number)
		}
	}

	return acc
}

func parseNumberAndSign(str string) (int, string) {
	var sign string
	var number int

	if string(str[4]) == "+" {
		sign = "+"
	}
	if string(str[4]) == "-" {
		sign = "-"
	}

	if len(str) == 7 {
		numberxd, _ := strconv.Atoi(string(str[5]))
		number = numberxd
	}
	if len(str) == 8 {
		numberxd, _ := strconv.Atoi(string(str[5:7]))
		number = numberxd
	}
	if len(str) == 9 {
		numberxd, _ := strconv.Atoi(string(str[5:8]))
		number = numberxd
	}

	return number, sign
}
