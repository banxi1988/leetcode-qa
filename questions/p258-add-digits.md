Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


首先是一个常规解法：

```go
func addDigits(num int) int {
	for num > 9 {
		sum := 0
		for num > 9 {
			sum += num % 10
			num = num / 10
		}
		sum += num
		num = sum
	}
	return num
}
```

下面思考不用循环及递归的方法。
参考自： https://my.oschina.net/Tsybius2014/blog/497645
得到的解法是：

```go
func addDigits(num int) int {
	return (num-1)%9 + 1
}
```

