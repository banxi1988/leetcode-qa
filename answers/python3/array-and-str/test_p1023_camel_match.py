# coding: utf-8

__author__ = '代码会说话'

"""
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。
（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。
只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

 ["CompetitiveProgramming","CounterPick","ControlPanel"]
  "CooP"
C
  [false,false,true]
"""

from typing import List

class Fsm:
  def __init__(self,pattern:str):
    self.pattern = pattern
    self.N = len(pattern)
    self.reset()

  def reset(self):
    self.statei = -1
    self.nextstate = None

  def _can_auto_move_to_next(self):
    return self.statei < (self.N -1) and (not self.pattern[self.statei+1].isupper())

  def _next_state(self):
    if self.statei < (self.N - 1):
      return self.pattern[self.statei + 1]


  def move_to(self,ch:str):
    ns = self._next_state()
    if ch.isupper():
      if not ns:
        return False
      if ns != ch:
        return False
      self.statei += 1
    else:
      # 后面可以匹配什么问题的小写字符
      if ns == ch:
        if self._can_auto_move_to_next():
          self.statei += 1
    return True

  def match(self,query):
    self.reset()
    for ch in query:
      if not self.move_to(ch):
        return False
    return self.statei == self.N -1









class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    ans = [False] * len(queries)
    fsm = Fsm(pattern=pattern)
    for i,query in enumerate(queries):
      ans[i] = fsm.match(query)
    return ans



def test():
  s = Solution()
  true = True
  false = False
  assert s.camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"],
                      "CooP") == [false,false,true]
  assert s.camelMatch(["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"],
  "ksvjLiknTzqn") == [true,true,true,true,true,true]
  assert s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB") == [true,false,true,true,false]

  assert s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa") == [true,false,true,false,false]

  assert s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT") == [false,true,false,false,false]

