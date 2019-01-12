# coding: utf-8

__author__ = '代码会说话'

"""
给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。

 

示例 1
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2
输入:

  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。

 

提示： 假设任意子树元素和均可以用 32 位有符号整数表示。

"""

from tree_node import  *

from collections import Counter
class Solution:
  def findFrequentTreeSum(self, root:TreeNode) -> List[int]:
    if not root:
      return []
    sums = []
    def collect_sum(branch:TreeNode) -> int:
      if not branch:
        return 0
      sum_left = collect_sum(branch.left)
      sum_right = collect_sum(branch.right)
      sum = sum_left + sum_right + branch.val
      sums.append(sum)
      return sum
    collect_sum(root)

    counter = Counter(sums)
    pairs =  counter.most_common()
    max_count = pairs[0][1]
    result = []
    for pair in pairs:
      if pair[1] == max_count:
        result.append(pair[0])
      else:
        break
    return result

def test():
  s = Solution()
  t1 = make_simple_tree(5,2,-3)
  assert s.findFrequentTreeSum(t1) == [2,-3,4]

  t2 = make_simple_tree(5,2,-5)
  assert s.findFrequentTreeSum(t2) == [2]