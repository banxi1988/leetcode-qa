Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.

## 解题分析

相当于是求  s + (s + 1) + ... + e  = N
s 和 e 的各种不同的解。
已知 
s <= e 特殊情况是 s=e=N
而且 s +  (s+ 1) + ... + e 的求和公式是
(s + e) * ( e - s + 1)/ 2 = N
(s + e) * (e - s + 1) = 2N
se - s^2 + s + e^2 - es + e = 2N
e^2 -s^2 + (e+s) = 2N
e^2 - 2N + e = s^2 - s

通过上面程序，可以通过遍历 e 来判断是否有 s 的正整数解以此来判断。

```go
func hasPositiveIntRoot(left int) bool {
	// s^2 + (-1)s + (-left) = 0
	// b^2 - 4ac
	innerSquare := 1 + 4*left
	root := int(math.Sqrt(float64(innerSquare)))
	if root*root != innerSquare {
		return false
	}

	x1Denominator := 1 + root
	if x1Denominator > 0 && x1Denominator%2 == 0 {
		return true
	}
	return false
}

func consecutiveNumbersSum(N int) int {
	// e^2 - 2N + e = s^2 - s
	compCount := 1 // one for self
	for e := N - 1; e > 0; e-- {
		left := e*e - 2*N + e
		if left < 1 {
			continue
		}
		if hasPositiveIntRoot(left) {
			compCount++
		}
	}
	return compCount
}
```
此解法已知问题：
当 N 较大时， e^2 可能溢出。
当 N 较大时，遍历次数比较慢。

通过再引入一个方法来计算。
即遍历和是由多个数组成的情况来。

`(s + e) * (e - s + 1) = 2N`
其中 ` e -s + 1 = k, k > = 1`
`(s+ e )*k = 2N`

即 `s + e = 2N/k` 及 `e - s = k - 1` 
其中要求 2N 是 k 的倍数




