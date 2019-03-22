# coding: utf-8

__author__ = '代码会说话'

"""
115. 不同的子序列

给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:

输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""

from functools import lru_cache


class Solution:

  @lru_cache(maxsize=None)
  def numDistinct(self, s: str, t: str) -> int:
    NS = len(s)
    NT = len(t)
    if NS < NT:
      return 0
    if NS == NT:
      return 1 if s == t else 0
    if NT == 1:
      return s.count(t)
    count = 0
    for i, ch in enumerate(s):
      if ch == t[0]:
        count += self.numDistinct(s[i + 1:], t[1:])

    return count

  def numDistinct_v2(self, s: str, t: str) -> int:
    NS = len(s)
    NT = len(t)
    if NS < NT:
      return 0
    if NS == NT:
      return 1 if s == t else 0
    if NT == 1:
      return s.count(t)
    df = [[0] * (NS + 1) for _ in range(NT + 1)]
    for c in range(0, NS + 1):
      df[0][c] = 1

    for r in range(1, NT + 1):
      tch = t[r - 1]
      for c in range(r, NS + 1):
        sch = s[c - 1]
        if sch == tch:
          df[r][c] = df[r - 1][c - 1] + df[r][c - 1]
        else:
          df[r][c] = df[r][c - 1]
    return df[-1][-1]


def test():
  s = Solution()
  assert s.numDistinct(s="rabbbit", t="rabbit") == 3
  assert s.numDistinct(s="babgbag", t="bag") == 5
  assert s.numDistinct(
    s="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
    t=
    "bcddceeeebecbc") == 700531452

  assert s.numDistinct_v2(s="rabbbit", t="rabbit") == 3
  assert s.numDistinct_v2(s="babgbag", t="bag") == 5
  assert s.numDistinct_v2(
    s="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
    t=
    "bcddceeeebecbc")
