# coding: utf-8

__author__ = '代码会说话'

"""
115. 不同的子序列 递归和动态规划算法详解

给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

C(3,2) = C(3,1) = 3*2/2*1 = 3/1 = 3
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
  
1. a,  ab  0
2. ab ,ab   1
3. ab, ac   0
4. abcabda , a

   "",b,a,b,g,b,a,g              # 
""  1,1,1,1,1,1,1,1
b   0,1,1,2,2,3,3,3
a   0,0,1,1,1,1,4,4
g   0,0,0,0,1,1,1,5

"""

from functools import lru_cache

class Solution:

  @lru_cache(maxsize=None)
  def numDistinct(self, s: str, t: str) -> int:
    # print(s, t)
    slen = len(s)
    tlen = len(t)
    if tlen > slen:
      return 0
    if tlen == slen:
      return 1 if s == t else 0
    if tlen == 1:
      return s.count(t)

    tch = t[0]
    total_count = 0
    for i, ch in enumerate(s):
      if ch == tch:
        count = self.numDistinct(s[i + 1:], t[1:])
        total_count += count
    return total_count

  def numDistinct_v2(self, s: str, t: str) -> int:
    slen = len(s)
    tlen = len(t)

    df = [[0] * (slen + 1) for _ in range(tlen + 1)]
    for c in range(0, slen + 1):
      df[0][c] = 1

    for r in range(1, tlen + 1):
      tch = t[r - 1]
      for c in range(r, slen + 1):
        sch = s[c - 1]
        if tch == sch:
          df[r][c] = df[r][c - 1] + df[r - 1][c - 1]
        else:
          df[r][c] = df[r][c - 1]

    return df[-1][-1]


def test():
  s = Solution()
  # assert s.numDistinct(s="ababcabbbb", t="ab")
  # assert s.numDistinct(s="rabbbit", t="rabbit") == 3
  assert s.numDistinct(s="babgbag", t="bag") == 5
  # assert s.numDistinct(s="a", t="a") == 1
  # assert s.numDistinct(s="a", t="ab") == 0
  # assert s.numDistinct(s="abaa", t="a") == 3
  # assert s.numDistinct(s="abaa", t="ab") == 1
  assert s.numDistinct(
    s="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
    t=
    "bcddceeeebecbc") == 700531452

  assert s.numDistinct_v2(s="rabbbit", t="rabbit") == 3
  assert s.numDistinct_v2(s="babgbag", t="bag") == 5
  assert s.numDistinct_v2(
    s="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
    t=
    "bcddceeeebecbc") == 700531452
