# coding: utf-8

__author__ = '代码会说话'

"""
给定有效字符串 "abc"。

对于任何有效的字符串 V，我们可以将 V 分成两个部分 X 和 Y，使得 X + Y（X 与 Y 连接）等于 V。（X 或 Y 可以为空。）那么，X + "abc" + Y 也同样是有效的。

例如，如果 S = "abc"，则有效字符串的示例是："abc"，"aabcbc"，"abcabc"，"abcabcababcc"。无效字符串的示例是："abccba"，"ab"，"cababc"，"bac"。

如果给定字符串 S 有效，则返回 true；否则，返回 false。

 

示例 1：

输入："aabcbc"
输出：true
解释：
从有效字符串 "abc" 开始。
然后我们可以在 "a" 和 "bc" 之间插入另一个 "abc"，产生 "a" + "abc" + "bc"，即 "aabcbc"。
示例 2：

输入："abcabcababcc"
输出：true
解释：
"abcabcabc" 是有效的，它可以视作在原串后连续插入 "abc"。
然后我们可以在最后一个字母之前插入 "abc"，产生 "abcabcab" + "abc" + "c"，即 "abcabcababcc"。
示例 3：

输入："abccba"
输出：false
示例 4：

输入："cababc"
输出：false
 

提示：

1 <= S.length <= 20000
S[i] 为 'a'、'b'、或 'c'

abc
a abc bc
ab abc c
abc abc
abc abc

aaabcbcbc
a b c
a abc bc
a a abc bc bc

a b c 
a abc b  c 
a ab abc c b c

a b c 
a b abc c
a b ab abc c c
a b ab ab abc c c c c  
"""


class Solution:
  def isValid(self, S: str) -> bool:
    if len(S) < 3:
      return False

    # if S[0] == 'c' or S[0] == 'b' or S[-1] == 'a' or S[-1] == 'b':
    #   return False

    def is_valid(s: str) -> bool:
      ch_cnt = len(s)
      if ch_cnt == 0:
        return True
      if ch_cnt == 3:
        return s == 'abc'
      try:
        first_index = s.index('abc')
        remain_str = s[:first_index] + s[first_index + 3:]
        return is_valid(remain_str)
      except ValueError:
        return False

    return is_valid(S)


def test():
  s = Solution()
  assert s.isValid("aaabcbcbc")
  assert s.isValid("abcabcabc")
  assert s.isValid("aabcbc")
  assert s.isValid("cababc") == False
  assert s.isValid("abccba") == False
