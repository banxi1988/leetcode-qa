We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)


## 解答分析

1） 暴力解法

```go
func checkPerfectNumber(num int) bool {
	divisors := []int{1}
	for d := 2; d <= num/2; d++ {
		if num%d == 0 {
			divisors = append(divisors, d)
		}
	}
	sum := 0
	for i := 0; i < len(divisors); i++ {
		sum += divisors[i]
	}
	return sum == num
}

```
相当于是 O(N) 的复杂度，当数比较大时，容易超时。

> 一个偶数是完美数，当且仅当它具有如下形式： {\displaystyle 2^{n-1}(2^{n}-1)} 2^{{n-1}}(2^{n}-1)，其中 {\displaystyle 2^{n}-1} 2^{n}-1是素数，此事实的充分性由欧几里得证明，而必要性则由欧拉所证明。

于是可以得到如下的解法来计算某一个数是否是完全数。

```go
func checkPerfectNumber(num int) bool {
	for n := 2; n < 15; n++ {
		part1 := 1 << uint(n-1) // 2^(n-1)
		part2 := (1 << uint(n)) - 1 // 2^n - 1
		numn := part1 * part2
		if numn == num {
			return true
		} else if numn > num {
			return false
		}
	}
	return false
}
```