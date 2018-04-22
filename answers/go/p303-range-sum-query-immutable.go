package main

import "fmt"

type NumArray struct {
	Nums []int
}

func Constructor(nums []int) NumArray {
	return NumArray{Nums: nums}
}

func (this *NumArray) SumRange(i, j int) int {
	sum := 0
	for index := i; index <= j; index++ {
		sum += this.Nums[index]
	}
	return sum
}

func main() {
	obj := Constructor([]int{-2, 0, 3, -5, 2, -1})
	fmt.Println("1 -> ", obj.SumRange(0, 2))
	fmt.Println("-1 -> ", obj.SumRange(2, 5))
	fmt.Println("-3 -> ", obj.SumRange(0, 5))
}
