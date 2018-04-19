package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	numCount := len(nums)
	if numCount == 0 {
		return 0
	}
	robLast := nums[0]
	passLast := 0
	for i := 1; i < numCount; i++ {
		robi := nums[i] + passLast
		passi := max(robLast, passLast)
		robLast = robi
		passLast = passi
	}
	return max(robLast, passLast)

}

func main() {
	fmt.Println(" 11 -> ", rob([]int{1, 3, 2, 6, 7, 2}))

	arr2 := []int{114, 117, 207, 117, 235, 82, 90, 67, 143, 146, 53, 108, 200, 91, 80, 223, 58, 170, 110, 236, 81, 90, 222, 160, 165, 195, 187, 199, 114, 235, 197, 187, 69, 129, 64, 214, 228, 78, 188, 67, 205, 94, 205, 169, 241, 202, 144, 240}
	fmt.Println(" 4173 -> ", rob(arr2))

	arr3 := []int{155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79, 133, 66, 36, 165}
	fmt.Println(" 4517 -> ", rob(arr3))
}
