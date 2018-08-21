package leetcode

func search(nums []int, target int) int {
	numCount := len(nums)
	low := 0
	high := numCount - 1
	for low <= high {
		mid := (low + high) / 2
		midValue := nums[mid]
		if target == midValue {
			return mid
		} else if target > midValue {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}
