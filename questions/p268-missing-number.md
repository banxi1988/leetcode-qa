Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

首先想到的一个办法就是先排序。 然后再对比。

```go
func missingNumber(nums []int) int {
	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		if i != nums[i] {
			return i
		}
	}
	return len(nums)
}
```

关于 O(N) + O(1) 的算法的思考。

如果不考虑溢出的话，首先对 0...N 求和。
然后对 nums 求和，他们之间的差值就是缺失数。

```go
func missingNumber(nums []int) int {
	n := len(nums)
	sumn := n * (n + 1) / 2
	sum := 0
	for i := 0; i < n; i++ {
		sum += nums[i]
	}
	return sumn - sum
}

```

如果考虑溢出的话就不能使用求和的方式。

另一种办法是考虑使用位运算。