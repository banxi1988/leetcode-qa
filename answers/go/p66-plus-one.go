package main

import "fmt"

func plusOne(digits []int) []int {
	index := len(digits)
	extraAddValue := 1
	for index > 0{
		index -= 1
		if digits[index] + extraAddValue == 10{
			digits[index] = 0
			extraAddValue = 1
			continue
		}else{
			if extraAddValue > 0 {
				digits[index] += extraAddValue
			}
			extraAddValue = 0
			break
		}
	}
	if extraAddValue > 0 {
		return append(digits[:0],append([]int{extraAddValue},digits[0:]...)...)
	}else{
		return digits
	}
}

func main(){
	fmt.Println(plusOne([]int{0}))
	fmt.Println(plusOne([]int{1,3,5}))
	fmt.Println(plusOne([]int{1,9,9}))
	fmt.Println(plusOne([]int{1,3,9}))
	fmt.Println(plusOne([]int{9,9,9}))
	
}