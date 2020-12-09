package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

const reqSum = 2020

func main() {
	file, err := os.Open("input.txt")
	defer file.Close()

	if err != nil {
		log.Fatalf("failed to open input file")

	}

	scanner := bufio.NewScanner(file)
	var lines []string

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for _, ln := range lines {
		num, err := strconv.Atoi(ln)
		if err != nil {
			log.Fatalf("failed to read number from string")
			os.Exit(1)
		}
		diff := reqSum - num
		index, found := find(lines, strconv.Itoa(diff))
		if found {
			fmt.Println("found a pair!", num, lines[index])
			pair, _ := strconv.Atoi(lines[index])
			multiplication := num * pair
			fmt.Println("Multiplication is: ", multiplication)
			break
		}
	}
}

func find(slice []string, val string) (int, bool) {
	for i, item := range slice {
		if item == val {
			return i, true
		}
	}
	return -1, false
}
