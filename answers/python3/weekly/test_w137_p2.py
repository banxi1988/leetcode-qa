# coding: utf-8

__author__ = '代码会说话'

"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

 

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
 

提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。
"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter


class Solution:
  def removeDuplicates(self, S: str) -> str:
    chars = S
    while True:
      ans = []
      N = len(chars)
      prev = None
      deleted_count = 0
      for i in range(0,N):
        if prev is None:
          prev = chars[i]
        else:
          ch = chars[i]
          if ch == prev:
            deleted_count += 1
            prev = None
          else:
            ans.append(prev)
            prev = ch
      if prev:
        ans.append(prev)
      if deleted_count == 0:
        return ''.join(ans)
      else:
        chars = ans



def test():
  s = Solution()
  assert s.removeDuplicates("abbaca") == "ca"
  assert s.removeDuplicates("abbbaca") == "abaca"
