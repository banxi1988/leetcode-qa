Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 _ 1 + 2 _ 2 = 5
Example 2:
Input: 3
Output: False


## 解法说明

首先是一个会超时的暴力解法：

```go
func judgeSquareSum(c int) bool {
	rootc := int(math.Sqrt(float64(c))) + 1
	for a := 0; a < rootc; a++ {
		for b := 0; b < rootc; b++ {
			sum := a*a + b*b
			if sum == c {
				return true
			}
		}
	}
	return false
}
```

分析其中的数学特性。

