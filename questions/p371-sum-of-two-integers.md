Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

对于 a = 3,b = 3 来考虑。

### 考虑二进制操作的一些结果 。

```
a = 0b11
b = 0b11
a + b = 0b110

a ^ b = 0b00
a | b = 0b11
a & b = 0b11
```

直接的二进制操作无法得到想加的结果，因为二进制位操作无法进制。

但是在计算机内部，+，- 操作其实都是通过二进制来实现的。
但是计算内部中加法是分为两个部分来计算的。但是他们是按位计算的。
1）是加法计算（不包含进位）
2）进位计算。

```
比如 3 + 3 = 0b11 + 0b11
分为两次加法计算：
1.1）加法: 0b1 + 0b1 = 0b0  需要使用 异或操作。
1.2) 进位： 0b1 + 0b1 = 0b1 需要使用与操作。


```