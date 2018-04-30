package main

import "fmt"
import "strconv"
import "time"

func fizzBuzz(n int) []string {
	strs := make([]string, n)
	for num := 1; num < n+1; num++ {
		i := num - 1
		is3 := num%3 == 0
		is5 := num%5 == 0
		if is3 && is5 {
			strs[i] = "FizzBuzz"
		} else if is3 {
			strs[i] = "Fizz"
		} else if is5 {
			strs[i] = "Buzz"
		} else {
			strs[i] = strconv.Itoa(num)
		}
	}
	return strs
}

func main() {
	start := time.Now()
	fmt.Println(fizzBuzz(200))
	elapsed := time.Since(start)
	fmt.Println("spend :", elapsed)
}
