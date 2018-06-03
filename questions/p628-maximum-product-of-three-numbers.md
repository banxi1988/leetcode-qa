Given an integer array, find three numbers whose product is maximum and output the maximum product.

```
Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
```

**Note:**

> The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
> Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

## 解法说明

数字中有负数，考虑到负负得正。 所以有二种情况。

* a) 三个最大的正整数。
* b) 一个最大的正整数，两个最小的负数。

我们要做的是找出两个最小的数，三个最大的数，然后看他们哪种情况的乘积大一些。
