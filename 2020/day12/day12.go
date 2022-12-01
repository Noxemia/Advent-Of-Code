package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func main() {
	readData, err := ioutil.ReadFile("day12input.txt")
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

	/*for _, row := range data {
		fmt.Println(row)
	}*/

	var instructions []string
	var values []int
	for _, row := range data {
		value, _ := strconv.Atoi(row[1:])
		values = append(values, value)
		instructions = append(instructions, string(row[0]))
	}

	/*for i := range instructions {
		fmt.Println(instructions[i], " - ", values[i])
	}*/

	heading := 90
	//heading = (heading + 270) % 360
	var xcoord int
	var ycoord int

	// p1
	for i := range instructions {

		// if instruction is forward, reading heading and move
		if instructions[i] == "F" {
			if heading == 0 {
				xcoord += values[i]
			}
			if heading == 90 {
				ycoord += values[i]
			}
			if heading == 180 {
				xcoord -= values[i]
			}
			if heading == 270 {
				ycoord -= values[i]
			}

		}
		// if instruction is rotate, add the degrees and mod 360
		if instructions[i] == "R" {
			heading = (heading + values[i]) % 360
		}
		if instructions[i] == "L" {
			heading = (heading + (360 - values[i])) % 360
		}
		if instructions[i] == "N" {
			ycoord += values[i]
		}
		if instructions[i] == "E" {
			xcoord += values[i]
		}
		if instructions[i] == "S" {
			ycoord -= values[i]
		}
		if instructions[i] == "W" {
			xcoord -= values[i]
		}
		//fmt.Println(xcoord, ycoord)

	}

	fmt.Println(Abs(xcoord), Abs(ycoord), Abs(xcoord)+Abs(ycoord))

	waypointy := 1
	waypointx := 10
	distancex := 0
	distancey := 0

	for i := range instructions {
		if instructions[i] == "F" {
			distancey += waypointy * values[i]
			distancex += waypointx * values[i]
		}
		if instructions[i] == "R" {
			for j := 0; j < (values[i] / 90); j++ {
				copy := waypointy
				waypointy = -waypointx
				waypointx = copy
			}
		}
		if instructions[i] == "L" {
			for j := 0; j < (values[i] / 90); j++ {
				copy := waypointy
				waypointy = waypointx
				waypointx = -copy
			}
		}
		if instructions[i] == "N" {
			waypointy += values[i]
		}
		if instructions[i] == "E" {
			waypointx += values[i]
		}
		if instructions[i] == "S" {
			waypointy -= values[i]
		}
		if instructions[i] == "W" {
			waypointx -= values[i]
		}
		fmt.Println(distancey, distancex, waypointy, waypointx)
	}
	fmt.Println(distancex, distancey, Abs(distancex)+Abs(distancey))

}

func rotateCounterClockwise(x float64, y float64, deg float64) []float64 {

	newX := x*math.Cos(deg) - y*math.Sin(deg)
	newY := x*math.Sin(deg) + y*math.Cos(deg)
	var res []float64
	res = append(res, newX)
	res = append(res, newY)

	return res
}

// Abs returns the absolute value of a int
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x

}
