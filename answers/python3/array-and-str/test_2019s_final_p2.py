# coding: utf-8

__author__ = '代码会说话'

"""
给出长度相同的两个字符串：A 和 B，其中 A[i] 和 B[i] 是一组等价字符。举个例子，如果 A = "abc" 且 B = "cde"，那么就有 'a' == 'c', 'b' == 'd', 'c' == 'e'。

等价字符遵循任何等价关系的一般规则：

自反性：'a' == 'a'
对称性：'a' == 'b' 则必定有 'b' == 'a'
传递性：'a' == 'b' 且 'b' == 'c' 就表明 'a' == 'c'
例如，A 和 B 的等价信息和之前的例子一样，那么 S = "eed", "acd" 或 "aab"，这三个字符串都是等价的，而 "aab" 是 S 的按字典序最小的等价字符串

利用 A 和 B 的等价信息，找出并返回 S 的按字典序排列最小的等价字符串。

 

示例 1：

输入：A = "parker", B = "morris", S = "parser"
输出："makkek"
解释：根据 A 和 B 中的等价信息，我们可以将这些字符分为 [m,p], [a,o], [k,r,s], [e,i] 共 4 组。每组中的字符都是等价的，并按字典序排列。所以答案是 "makkek"。
示例 2：

输入：A = "hello", B = "world", S = "hold"
输出："hdld"
解释：根据 A 和 B 中的等价信息，我们可以将这些字符分为 [h,w], [d,e,o], [l,r] 共 3 组。所以只有 S 中的第二个字符 'o' 变成 'd'，最后答案为 "hdld"。
示例 3：

输入：A = "leetcode", B = "programs", S = "sourcecode"
输出："aauaaaaada"
解释：我们可以把 A 和 B 中的等价字符分为 [a,o,e,r,s,c], [l,p], [g,t] 和 [d,m] 共 4 组，因此 S 中除了 'u' 和 'd' 之外的所有字母都转化成了 'a'，最后答案为 "aauaaaaada"。
 

提示：

字符串 A，B 和 S 仅有从 'a' 到 'z' 的小写英文字母组成。
字符串 A，B 和 S 的长度在 1 到 1000 之间。
字符串 A 和 B 长度相同。
"""

from collections import defaultdict


class UF:
  def __init__(self):
    self.group_to_sets = defaultdict(set)
    self.ch_to_group = {}

  def union(self, a, b):
    ga = self.ch_to_group.get(a)
    gb = self.ch_to_group.get(b)
    if ga and gb:
      if ga == gb:
        return
        # merge  gb to ga
      aset = self.group_to_sets[ga]
      bset = self.group_to_sets[gb]
      aset.update(bset)
      for bm in bset:
        self.ch_to_group[bm] = ga
      del self.group_to_sets[gb]
    elif ga is None and gb is None:
      self.ch_to_group[a] = a
      self.ch_to_group[b] = a
      self.group_to_sets[a] = {a, b}
    else:
      if ga:
        aset = self.group_to_sets[ga]
        aset.add(b)
        self.ch_to_group[b] = ga
      else:
        bset = self.group_to_sets[gb]
        bset.add(a)
        self.ch_to_group[a] = gb

  def calc_ch_to_min(self):
    ch_to_min = {}
    for _, chset in self.group_to_sets.items():
      if not chset:
        continue
      min_ch = min(chset)
      for ch in chset:
        ch_to_min[ch] = min_ch
    return ch_to_min


class Solution:
  def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
    uf = UF()
    for i in range(len(A)):
      uf.union(A[i], B[i])
    ch_to_min = uf.calc_ch_to_min()
    s_min_chs = []
    for ch in S:
      min_ch = ch_to_min.get(ch)
      if min_ch:
        s_min_chs.append(min_ch)
      else:
        s_min_chs.append(ch)
    return ''.join(s_min_chs)


def test():
  s = Solution()
  assert s.smallestEquivalentString(A="ceihfgechfcbjhadaibhghcbdhfaecdaijigaaafcadebciabb",
                                    B="gafbfceidigjceeigcddichdhhbgibjbaagbfciiecjaiajahh",
                                    S="eoiloytuagirigmbarebhzgveiavyruxlrxzbommyfjjngfktd") == "aoaloytuaaaraamaaraaazavaaavyruxlrxzaommyaaanaakta"
  assert s.smallestEquivalentString(A="eachghbdabchffhaadfcdfdceacaebaghdhbdcehbbbgabagff",
                                    B="gdchgcgbhbaahdeddaeafdcaceeabgbeefcdahedfbbghcecaf",
                                    S="pacwwgbkcengcwxerkxqlwtetqwkqjrzsqmcsuhoexbacnveyi") == "paawwaakaanaawxarkxqlwtatqwkqjrzsqmasuaoaxaaanvayi"
  assert s.smallestEquivalentString(A="parker", B="morris", S="parser") == "makkek"
  assert s.smallestEquivalentString(A="hello", B="world", S="hold") == "hdld"
  assert s.smallestEquivalentString(A="leetcode", B="programs", S="sourcecode") == "aauaaaaada"
