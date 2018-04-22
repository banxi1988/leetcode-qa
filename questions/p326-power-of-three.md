Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

首先是一个有循环的解法：

```go
func isPowerOfThree(n int) bool {
	if n == 0 {
		return false
	}
	if n == 1 {
		return true
	}
	if n%3 != 0 {
		return false
	}
	num := 3
	for num < n {
		num *= 3
	}
	return n == num

}
```

不用循环，我想到的只有利用数学的一些知识。
比如 Log3(9) = 2,也就是说如果数字 N 以 3为底的对数是一个整数，也就是说 N 是 3 的幂。
幂运算是对象的逆运算。 但是一般的库都没有提供以 3 为底的对数，而是 以 `2,e,10` 为底的对数。

不过对数中有一个换底公式：

参考 [对数](https://zh.wikipedia.org/wiki/%E5%AF%B9%E6%95%B0)

也就是 Log(a)(x) = log(b)(x) / log(b)(a)
于是我们就可以用以 `2,e,10` 为底的对数计算函数来计算 `Log(3)(9)`.

但是这样计算出来的数，有一个问题就是精度问题：

```go
log3 := math.Log10(float64(n)) / math.Log10(float64(3))
// 3.0000000000000004 3   -4.440892098500626e-16
```
计算出来按理想来说应该是 `3.0` 但是其实是 `3.0000000000000004`

可以通过 `epsilon := math.Nextafter(1.0, 2.0) - 1.0` 来计算最小的浮点数。
即 `2.220446049250313e-16` 但是发现不少相减计算都大于 `epsilon` 所以又对 `epsilon` 的比较进行了宽容处理。
```
243 5.000000000000001 5 8.881784197001252e-16 2.220446049250313e-16
4782969 14.000000000000004 14 3.552713678800501e-15 2.220446049250313e-16
```

于是得到以下代码：
```go
func isPowerOfThree(n int) bool {
	if n == 0 {
		return false
	}
	if n == 1 {
		return true
	}
	if n%3 != 0 {
		return false
	}
	log3 := math.Log10(float64(n)) / math.Log10(float64(3))
	log3if := float64(int(log3))
	epsilon := math.Nextafter(1.0, 2.0) - 1.0
	diff := log3 - log3if
	fmt.Println(n, log3, log3if, diff, epsilon)
	return diff <= epsilon*100
	// 3.0000000000000004 3   -4.440892098500626e-16
	// return log3 == log3if

```