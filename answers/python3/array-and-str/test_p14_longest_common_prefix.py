# coding: utf-8

__author__ = '代码会说话'

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""

from typing import List

class Solution:
  def longestCommonPrefix(self, strs:List[str]):
    if not strs:
      return ""
    if len(strs) == 1:
      return strs[0]
    i = 0
    str1 = strs[0]
    max_chars = min(len(s) for s in strs)
    other_strs = strs[1:]
    while i < max_chars:
      if all(stri[i] == str1[i] for stri in other_strs):
        i+=1
        continue
      else:
        break
    return str1[:i]


def test():
  s = Solution()
  assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
  assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
  assert s.longestCommonPrefix(["abc"]) == "abc"

