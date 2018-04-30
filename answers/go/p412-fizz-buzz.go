package main

import "fmt"
import "strconv"

func fizzBuzz(n int) []string {
	strs := []string{}
	for num := 1; num < n+1; num++ {
		is3 := num%3 == 0
		is5 := num%5 == 0
		if is3 && is5 {
			strs = append(strs, "FizzBuzz")
		} else if is3 {
			strs = append(strs, "Fizz")
		} else if is5 {
			strs = append(strs, "Buzz")
		} else {
			strs = append(strs, strconv.Itoa(num))
		}
	}
	return strs
}

func main() {
	fmt.Println(fizzBuzz(15))
}
