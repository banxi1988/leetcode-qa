package main

import (
	"fmt"
)

func shortestPathLength(graph [][]int) int {
	return 0
}

func main() {
	arrA := [][]int{
		{1, 2, 3},
		{0},
		{0},
		{0},
	}
	fmt.Println("4 -> ", shortestPathLength(arrA))
	arrB := [][]int{
		{1},
		{0, 2, 4},
		{1, 3, 4},
		{2},
		{1, 2},
	}
	fmt.Println("4 -> ", shortestPathLength(arrB))

	myStack := &Stack{}
	myStack.Push('a')
	fmt.Println("myStack:", myStack.chars)
}

type Stack struct {
	chars []byte
}

func (this *Stack) Push(char byte) {
	this.chars = append(this.chars, char)
}
