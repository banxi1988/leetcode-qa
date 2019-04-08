# coding: utf-8

__author__ = '代码会说话'

"""
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。
"""

from typing import List
import re

class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    re_patterns = []
    if pattern:
      re_patterns.append('[a-z]*')
    for i,ch in enumerate(pattern):
      re_patterns.append(ch)
      re_patterns.append('[a-z]*')

    re_pattern =  re.compile(''.join(re_patterns))
    results = [False] * len(queries)
    for i,q in enumerate(queries):
      results[i] = re_pattern.fullmatch(q) is not None
    return results


def test():
  s = Solution()
  true = True
  false = False
  assert s.camelMatch(["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"],
  "ksvjLiknTzqn") == [true,true,true,true,true,true]
  assert s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB") == [true,false,true,true,false]

  assert s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa") == [true,false,true,false,false]

  assert s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT") == [false,true,false,false,false]

  assert s.camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"],
  "CooP") == [false,false,true]
