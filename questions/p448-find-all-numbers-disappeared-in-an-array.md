Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


### 空间 O(N) 的解法

首先最简单的就是使用一个 hash 表。 用来判断不存在其中的数。

```go
func findDisappearedNumbers(nums []int) []int {
	map1 := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		map1[num] = true
	}
	results := []int{}
	for num := 1; num < (len(nums) + 1); num++ {
		_, ok := map1[num]
		if !ok {
			results = append(results, num)
		}
	}
	return results
}


```

### 空间 O(1) 的解法
这就需要利用 1...N 数字之间的特点。来查找。
利用和和乘法话，相当于是解多元一次方程，多元只有一个等式，计算不出来。

上网搜索一下，有提取利用正负表的概念的说法：
https://www.polarxiong.com/archives/LeetCode-448-find-all-numbers-disappeared-in-an-array.html

针对本题的具体情况，可以将 map 的这种思想放到数组中来实现。 之前是将 (index + 1) 作为 key 来判断某一个数是否存在。
这里是遍历的时候直接将 (index) 对应的数设置为对应值的负数。（对应值包含了了索引信息）
不能去掉或者设置为其他值，但是可以设置为负数。这样当遍历对此负数值，还可以方便的将对应的索引信息转换出来。


```go
func findDisappearedNumbers(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		numIndex := num - 1
		if num < 0 {
			numIndex = -num - 1
		}
		if nums[numIndex] > 0 {
			nums[numIndex] = -nums[numIndex]
		}
	}
	results := []int{}
	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			results = append(results, i+1)
		}
	}
	return results
}
```