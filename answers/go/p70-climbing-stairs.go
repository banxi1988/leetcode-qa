package main

import "fmt"

func climbStairs(n int) int {
	switch n {
	case 1:
		return 1
	case 2:
		return 2
	case 3:
		return 3
	case 4:
		return 5
	default:
		f3 := 3
		f4 := 5
		f5 := 0
		for i := 5; i <= n; i++ {
			f5 = f3 + f4
			f3 = f4
			f4 = f5
		}
		return f5
	}
}

func main() {
	fmt.Println("2 -> 2 ", climbStairs(2))
	fmt.Println("3 -> 3 ", climbStairs(3))
	fmt.Println("4 -> 5 ", climbStairs(4))
	fmt.Println("5 -> 8 ", climbStairs(5))
}
