You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

首先得出一个递归的解法:
主要逻辑是走第一步有两种走法即走2阶还是走一阶。然后求和。

```go
func climbStairs(n int) int {
   switch n {
	case 1:
		return 1
	case 2:
		return 2
	case 3:
		return 3
	case 4:
		return 5
	default:
		return climbStairs(n-2) + climbStairs(n-1)
	}
}
```

然后将递归的写法转成迭代的方法。

```go
func climbStairs(n int) int {
	switch n {
	case 1:
		return 1
	case 2:
		return 2
	case 3:
		return 3
	case 4:
		return 5
	default:
		f3 := 3
		f4 := 5
		f5 := 0
		for i := 5; i <= n; i++ {
			f5 = f3 + f4
			f3 = f4
			f4 = f5
		}
		return f5
	}
}

```