package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {

	data, err := ioutil.ReadFile("day3input.txt")
	if err != nil {
		fmt.Println("file not found")
		return
	}
	stringSplited := strings.Split(string(data), "\n")

	posx := 0
	counter := 0
	check := "#"
	for _, l := range stringSplited {
		fmt.Println(posx, len(l))
		if string(l[posx]) == check {
			counter = counter + 1
		}
		posx = posx + 3
		if posx >= len(l)-1 {
			posx = posx - len(l) + 1
		}
	}
	fmt.Println("#" == "#")
	fmt.Println(counter)

}
