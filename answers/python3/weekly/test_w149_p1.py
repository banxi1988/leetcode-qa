# coding: utf-8

__author__ = '代码会说话'

"""

"""


from datetime import datetime

class Solution:
  def ordinalOfDate(self, date: str) -> int:
    d  = datetime.strptime(date,'%Y-%m-%d')
    dofy = d.strftime('%j')
    return int(dofy)



def test():
  s = Solution()
  assert s.ordinalOfDate(date = "2019-01-09") == 9
  assert s.ordinalOfDate(date = "2019-02-10") == 41
  assert s.ordinalOfDate(date = "2003-03-01") == 60
  assert s.ordinalOfDate(date = "2004-03-01") == 61
