Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.


一开始利用不停移到最后一个到前面来处理：

```go
func rotate(nums []int, k int) {
	numCount := len(nums)
	index := numCount - 1
	for k > 0 {
		nums = append([]int{nums[index]}, nums[:index]...)
		k--
	}
}
```

但是这个导致没有修改到原来的切片。所以通过 `append` 的方式是行不通的。所以只能通过 swap 的方式。