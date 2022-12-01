package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	readData, err := ioutil.ReadFile("day11input.txt")
	if err != nil {
		fmt.Println("error on reading file", err)
		return
	}
	dataStrings := strings.Split(string(readData), "\n")
	var p1Map []string
	var p2Map []string

	for _, row := range dataStrings {
		p1Map = append(p1Map, row[0:93])
		p2Map = append(p2Map, row[0:93])
	}
	//fmt.Println(countOccupied2(2, 0, p2Map))
	//fmt.Println(diagTraverse(6, 0, 1, 1, p2Map))
	//part1(p1Map)
	part2(p2Map)
}

func part2(seatMap []string) {
	for i := 0; i < 1000; i++ {
		newMap := updateMap2(seatMap)
		//fmt.Println("------------------------")
		for i, row := range newMap {
			//fmt.Println(row)
			seatMap[i] = row
		}
	}

	count := 0
	for _, row := range seatMap {
		for _, char := range row {
			if string(char) == "#" {
				count++
			}
		}
	}
	fmt.Println(count)
}

func updateMap2(seatMap []string) []string {
	var newSeatmap []string

	for yindex, row := range seatMap {
		var newRow string
		for xindex, char := range row {
			amtOccupied := countOccupied2(xindex, yindex, seatMap) // Count all #:s around the current co-or

			if string(char) == "L" {
				if amtOccupied == 0 {
					newRow = newRow + "#"
				} else {
					newRow = newRow + "L"
				}
			} else if string(char) == "#" {
				if amtOccupied >= 5 {
					newRow = newRow + "L"
				} else {
					newRow = newRow + "#"
				}
			} else if string(char) == "." {
				newRow = newRow + "."
			}

		}

		newSeatmap = append(newSeatmap, newRow)
	}
	return newSeatmap
}

func countOccupied2(xindex int, yindex int, seatMap []string) int {

	rl := seatMap[yindex] // right left
	var tb string         //top bottom

	for _, row := range seatMap {
		tb += string(row[xindex])
	}

	//fmt.Println(tb)
	/// Direction relative to puzzle input
	ru := diagTraverse(xindex, yindex, 1, -1, seatMap) // TO RIGHT UP
	rd := diagTraverse(xindex, yindex, 1, 1, seatMap)  // TO RIGHT DOWN

	lu := diagTraverse(xindex, yindex, -1, -1, seatMap) // TO LEFT UP
	ld := diagTraverse(xindex, yindex, -1, 1, seatMap)  // TO LEFT DOWN

	r := straightTraverse(xindex, 1, rl)  // to right
	l := straightTraverse(xindex, -1, rl) // to left
	d := straightTraverse(yindex, 1, tb)  // down
	u := straightTraverse(yindex, -1, tb) // up

	//fmt.Println(u, ru, r, rd, d, ld, l, lu)

	return rd + ru + ld + lu + r + l + u + d
}

func diagTraverse(xindex int, yindex int, xmod int, ymod int, seatMap []string) int {
	if (yindex+ymod > len(seatMap)-1) || (yindex+ymod < 0) {
		return 0
	} else if (xindex+xmod > len(seatMap[0])-1) || (xindex+xmod < 0) {
		return 0
	}

	modChar := string(seatMap[yindex+ymod][xindex+xmod])
	if modChar == "#" {
		return 1
	}
	if modChar == "L" {
		return 0
	}
	return diagTraverse(xindex+xmod, yindex+ymod, xmod, ymod, seatMap)
}

func straightTraverse(index int, mod int, str string) int {
	if index+mod > len(str)-1 || index+mod < 0 {
		return 0
	}

	if string(str[index+mod]) == "#" {
		return 1
	}
	if string(str[index+mod]) == "L" {
		return 0
	}

	return straightTraverse(index+mod, mod, str)

}

func part1(seatMap []string) {
	for i := 0; i < 100; i++ {
		newMap := updateMap1(seatMap)

		for i, row := range newMap {
			seatMap[i] = row
		}
	}

	count := 0
	for _, row := range seatMap {
		for _, char := range row {
			if string(char) == "#" {
				count++
			}
		}
	}
	fmt.Println(count)

}

func updateMap1(seatMap []string) []string {
	var newSeatmap []string

	for yindex, row := range seatMap {
		var newRow string
		for xindex, char := range row {

			amtOccupied := countOccupied1(xindex, yindex, seatMap) // Count all #:s around the current co-or

			if string(char) == "L" {
				if amtOccupied == 0 {
					newRow = newRow + "#"
				} else {
					newRow = newRow + "L"
				}
			} else if string(char) == "#" {
				if amtOccupied >= 4 {
					newRow = newRow + "L"
				} else {
					newRow = newRow + "#"
				}
			} else if string(char) == "." {
				newRow = newRow + "."
			}

		}

		newSeatmap = append(newSeatmap, newRow)
	}
	return newSeatmap
}

func getSeatAt(x int, y int, seatMap []string) string {

	// if out of bounds, return a sitting position
	if (y > len(seatMap)-1) || (y < 0) {
		return "."
	} else if (x > len(seatMap[0])-1) || (x < 0) {
		return "."
	}
	// if in bounds, return the actual
	return string(seatMap[y][x])

}

func generateSeatList(x int, y int) [][]int {
	var res [][]int

	/// Create a list of all coordinates around the given coordinate. Coordinates might be negative but that is handled by getSeatAt
	var placeholder1 []int
	placeholder1 = append(placeholder1, 0)
	placeholder1 = append(placeholder1, 0)
	var placeholder2 []int
	placeholder2 = append(placeholder2, 0)
	placeholder2 = append(placeholder2, 0)
	var placeholder3 []int
	placeholder3 = append(placeholder3, 0)
	placeholder3 = append(placeholder3, 0)
	var placeholder4 []int
	placeholder4 = append(placeholder4, 0)
	placeholder4 = append(placeholder4, 0)
	var placeholder5 []int
	placeholder5 = append(placeholder5, 0)
	placeholder5 = append(placeholder5, 0)
	var placeholder6 []int
	placeholder6 = append(placeholder6, 0)
	placeholder6 = append(placeholder6, 0)
	var placeholder7 []int
	placeholder7 = append(placeholder7, 0)
	placeholder7 = append(placeholder7, 0)
	var placeholder8 []int
	placeholder8 = append(placeholder8, 0)
	placeholder8 = append(placeholder8, 0)
	placeholder1[1] = y - 1
	placeholder1[0] = x - 1
	res = append(res, placeholder1)
	placeholder2[1] = y - 1
	placeholder2[0] = x
	res = append(res, placeholder2)
	placeholder3[1] = y - 1
	placeholder3[0] = x + 1
	res = append(res, placeholder3)
	placeholder4[1] = y
	placeholder4[0] = x - 1
	res = append(res, placeholder4)
	placeholder5[1] = y
	placeholder5[0] = x + 1
	res = append(res, placeholder5)
	placeholder6[1] = y + 1
	placeholder6[0] = x - 1
	res = append(res, placeholder6)
	placeholder7[1] = y + 1
	placeholder7[0] = x
	res = append(res, placeholder7)
	placeholder8[1] = y + 1
	placeholder8[0] = x + 1
	res = append(res, placeholder8)

	return res
}

func countOccupied1(x int, y int, seatMap []string) int {

	nearbySeats := generateSeatList(x, y)
	count := 0
	for _, seatCoords := range nearbySeats {

		if getSeatAt(seatCoords[0], seatCoords[1], seatMap) == "#" {
			count++
		}
	}

	return count

}
