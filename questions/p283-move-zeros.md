Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

首先是一个常规的两层循环的操作：

```go
func moveZeroes(nums []int) {
	numCount := len(nums)

	for i := 0; i < numCount-1; i++ {
		num := nums[i]
		if num != 0 {
			continue
		}
		for j := i + 1; j < numCount; j++ {
			numj := nums[j]
			if numj != 0 {
				nums[i] = numj
				nums[j] = 0
				break
			}
		}
		// fmt.Println(nums)
	}
}
```