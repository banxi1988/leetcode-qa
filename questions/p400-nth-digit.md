Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


解释分析笔记： 首先进行如下分析，各个数区间中 数字的个数：

```
1-9:        9 * 1 个
10-99:      90 * 2 =  189 个
100-999:    900 * 3 = 2700 个
1000-9999:  9000 * 4 = 36000 个
```
这个各个区间中数字的个数是有规则可以计算。
对于 K 位数有 
    (9) * (10^(k-1)) * K
通过循环减法，可以确定 第 N 个数字在哪一个数的区间。
然后再通过在对应区间的索引值来判断是对应区间在哪一个数。
然后再计算在对应的数中的索引。具体代码见解答。