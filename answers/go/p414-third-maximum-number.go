package main

import "fmt"

const (
	maxInt = int(^uint(0) >> 1)
	minInt = -maxInt - 1
)

func thirdMax(nums []int) int {
	max1 := minInt
	max2 := minInt
	max3 := minInt
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if num >= max1 {
			if num > max1 {
				max3 = max2
				max2 = max1
				max1 = num
			}
		} else if num >= max2 {
			if num > max2 {
				max3 = max2
				max2 = num
			}
		} else if num >= max3 {
			max3 = num
		}
	}
	if max3 != minInt {
		return max3
	}
	return max1
}

func main() {
	fmt.Println("1 -> ", thirdMax([]int{3, 2, 1}))
	fmt.Println("2 -> ", thirdMax([]int{1, 2}))
	fmt.Println("1 -> ", thirdMax([]int{2, 2, 3, 1}))
	fmt.Println("5 -> ", thirdMax([]int{5, 2, 2}))
}
