package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	readData, err := ioutil.ReadFile("day10input.txt")
	if err != nil {
		fmt.Println("error on reading file", err)
		return
	}
	rawData := strings.Split(string(readData), "\n")
	// Parse to remove newlines of end
	// Add extra char on last line to counter newline signs
	var data []string
	for _, row := range rawData {
		data = append(data, row[0:len(row)-1])
	}
}
