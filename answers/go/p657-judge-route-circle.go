package main

import (
	"fmt"
)

func judgeCircle(moves string) bool {
	x := 0
	y := 0
	for _, ch := range moves {
		switch ch {
		case 'L':
			x++
		case 'R':
			x--
		case 'U':
			y++
		case 'D':
			y--
		default:
			break
		}
	}
	return x == 0 && y == 0

}

func main() {
	fmt.Println("true ->", judgeCircle("UD"))
	fmt.Println("true ->", judgeCircle("UDUD"))
	fmt.Println("false ->", judgeCircle("LLLRR"))
	fmt.Println("true ->", judgeCircle("LLRR"))
	fmt.Println("true ->", judgeCircle("LDRU"))
	fmt.Println("false ->", judgeCircle("LDR"))
}
