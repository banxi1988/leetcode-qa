
# LeetCode Python 一行代码求解系列

1. [561 数组拆分I](https://leetcode-cn.com/problems/array-partition-i)

```python
class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
```