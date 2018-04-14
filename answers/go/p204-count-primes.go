package main

import "fmt"

func countPrimes(n int) int {
	filtered := make([]bool, n)
	for num := 2; num < n; num++ {
		if filtered[num] == false {
			pow2 := num * num
			for pow2 < n {
				filtered[pow2] = true
				pow2 += num
			}
		}
	}
	count := 0
	for num := 2; num < n; num++ {
		if filtered[num] == false {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println("0 -> ", countPrimes(1))
	fmt.Println("0 -> ", countPrimes(2))
	fmt.Println("1 -> ", countPrimes(3))
	fmt.Println("2 -> ", countPrimes(4))
	fmt.Println("2 -> ", countPrimes(5))
	fmt.Println("3 -> ", countPrimes(6))
	fmt.Println("3 -> ", countPrimes(7))
	fmt.Println("4 -> ", countPrimes(8))
	fmt.Println("5 -> ", countPrimes(12))
	fmt.Println("6 -> ", countPrimes(14))
}
