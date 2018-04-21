package main

import "fmt"

func canWinNim(n int) bool {
	return n%4 != 0
}

func main() {
	fmt.Println("false ->", canWinNim(1348820612))
	fmt.Println("true ->", canWinNim(1))
	fmt.Println("true ->", canWinNim(5))
	fmt.Println("true ->", canWinNim(6))
	fmt.Println("true ->", canWinNim(7))
	fmt.Println("false ->", canWinNim(8))
	fmt.Println("true ->", canWinNim(35))
}
