Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].


## 解法分析

首先是写了一个穷举的写法：

```go
func isPalindrome(str string) bool {
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		if str[i] != str[j] {
			return false
		}
	}
	return true
}

func isProductPalindrome(num1, num2 int) bool {
	product := num1 * num2
	str := strconv.Itoa(product)
	return isPalindrome(str)
}

func largestPalindrome(n int) int {
	productMod := 0
	digitCount := n
	base := 1
	for digitCount > 1 {
		base *= 10
		digitCount--
	}
	upbound := base*10 - 1
	for i := upbound; i > (base - 1); i-- {
		found := false
		for j := i; j > (base - 1); j-- {
			if isProductPalindrome(i, j) {
				found = true
				fmt.Println(i, j, " -> ", i*j)
				productMod = (i * j) % 1337
				break
			}
		}
		if found {
			break
		}
	}
	return productMod
}
```

从输出的计算结果来看，感觉是 OK 的。

```
9 1  ->  9
 9 ->  9
99 91  ->  9009
 987 ->  987
995 583  ->  580085
 (1164?) 123 ->  1164
9999 9901  ->  99000099
 597 ->  597
99995 58663  ->  5866006685
 742 ->  742
999999 999001  ->  999000000999
 1218 ->  1218
9999995 5866663  ->  58666600666685
 284 ->  284
99999999 99990001  ->  9999000000009999
 475 ->  475
```

但是提交之后没有被 AC。 对于 3 位数，其结果的模为 `123` 然后上面的计算结果显示是 1164.

另外一个问题就是当 n 等于 8 的时候计算过程是比较慢的。耗时是比较长的。

参考其他的解法发现 3 位数最大回文数是 : `906609`

再仔细思考，上面的解法的逻辑问题在于。当 `num1 = 995` 时对应 `num2 = 583` 的是其发现的第一个回文数。
从循环上来看，也许存在 `num1 = 994` `num2 > 583` 这样的回文数。所以这样的一次循环无法计算出最大的回文数。

于是将核心循环改成下面的样子:

```go
	maxProduct := 0
	num1 := 0
	num2 := 0
	for i := upbound; i > downbound; i-- {
		for j := i; j > downbound; j-- {
			product := i * j
			if isProductPalindrome(product) {
				if product > maxProduct {
					num1 = i
					num2 = j
					maxProduct = product
				}
				break
			}
		}
	}
	fmt.Println(num1, " * ", num2, " = ", maxProduct)
	return (maxProduct % 1337)
```

得到： `993  *  913  =  906609`
可以看出最大回文数都是 9 开头的数的乘积。
1. `99 * 91  =  9009`
2. `993  *  913  =  906609`
3. `9999 9901  ->  99000099`
4. `99979  *  99681  =  9966006699`
5. `99999999 99990001  ->  9999000000009999`

### 构造回文数解法
经过搜索，发现一种先构造可能的最大回文数再确定其中一个数的解法。

对于2位数而言，最大回文数是 `9999`,然后再判断这个回文数是否有对 `x*y=9999` 在 10到99 之间的整数解。如果有的话，此时 `9999` 就是最大回文乘积。
 所以第一个遍历的条件是就是通过 `num = 99 ; num > 10; num--` ,然后根据 `num` 构造回文。当 `num=99` 时回文为 `9999` 当 `num=98` 时回文为 `9889`

即主要逻辑如下：

```go
func largestPalindrome(n int) int {
	upbound := int(math.Pow10(n)) - 1
	downbound := upbound / 10
	for i := upbound; i > downbound; i-- {
		palindrome := makePalindrome(i)
		for j := upbound; j > downbound; j-- {
			if palindrome%j == 0 {
				fmt.Println(palindrome, j)
				return palindrome % 1337
			}
		}
	}
	return 9
}
```

但是这里还有一个问题，以两个位数为例 第一个构造的最大乘积回文是 `9999` 此时 `i = 99`, 那当 `j=99` 时满足 `9999 % 99 == 0`
但是 `9999 / 99 = 101` 这个时候另一个值是大于 `99` 的。这样的话不符合要求。 所以还需要满足 `(palindrome/j) < j`;
这个公式转换之后又得到另一个形式，  `plaindrome < j*j`

修正之后得到如下代码：

```go
func largestPalindrome(n int) int {
	if n == 1{
		return 9
	}
	upbound := int(math.Pow10(n)) - 1
	downbound := upbound / 10
	for i := upbound; i > downbound; i-- {
		palindrome := makePalindrome(i)
		for j := upbound; j > downbound && palindrome < j*j; j-- {
			if palindrome%j == 0 {
				//fmt.Println(palindrome, j)
				return palindrome % 1337
			}
		}
	}
	return 0
}
```

其中外层循环是用来构造最大的回文数。第二个循环是用来查找乘积的最大的一个 N 位数因子。


