Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

**备注：**
对于字符串来的加法来说，字符串的最后才是低位，所以逆序计算。

```go
	for i, j := (num1Len - 1), (num2Len - 1); i > -1 || j > -1; i, j = i-1, j-1 {
    }
```

但是的时候需要将后面想加的插入在前面。

```go
		digitBytes = append([]byte{digitByte}, digitBytes...)
```

最后记得处理最后一个进位:

```go
	if carry > 0 {
		digitBytes = append([]byte{'1'}, digitBytes...)
	}

```