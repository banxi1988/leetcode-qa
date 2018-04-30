Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

## 分析

由于 O(N) 的时间复杂度，所以考虑选择三个变量来存储最大值(max1)，第二大值(max2)，和第三大值(max3)。
遍历每一个数(num)

### 如果一个数大于 max1
1) 其他的数字顺序后推。
max3 = max2
max2 = max1
max1 = num

### 如果一个数大于 max2
1）后面的数顺序后推
max3 = max2
max2 = num

### 如果一个数大于 max3
max3 = num


值得注意的是，对于等于的情况不能再将数据顺序后推。