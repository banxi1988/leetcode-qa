# coding: utf-8
from collections import defaultdict
from typing import NamedTuple

__author__ = '代码会说话'
"""
并查集介绍及应用 (1)

"""


class Student(NamedTuple):
  name: str
  province: str


def test_basic():
  s1 = Student('张三', '湖北')
  s2 = Student('李四', '湖北')
  s3 = Student('王五', '湖北')
  s4 = Student('李雷', '湖南')
  s5 = Student('胡二', '湖北')
  s6 = Student('赵六', '湖北')
  s7 = Student('李想', '湖南')
  s8 = Student('张进', '湖南')

  provinces = set([s.province for s in (s1, s2, s3, s4, s5, s6, s7, s8)])
  return len(provinces)


class Fellowship(NamedTuple):
  name1: str
  name2: str


from typing import List


class Solution:
  def findProvinceNum(self, fellowships: List[Fellowship]) -> int:
    fellow_to_lord = {}
    lord_to_fellows = defaultdict(set)
    for f in fellowships:
      lord1 = fellow_to_lord.get(f.name1)
      lord2 = fellow_to_lord.get(f.name2)
      if lord1 is None and lord2 is None:
        lord = f.name1
        fellow_to_lord[f.name1] = lord
        fellow_to_lord[f.name2] = lord
        lord_to_fellows[lord].add(f.name1)
        lord_to_fellows[lord].add(f.name2)
      elif not (lord1 and lord2):
        if lord1:
          fellow_to_lord[f.name2] = lord1
          lord_to_fellows[lord1].add(f.name2)
        else:
          fellow_to_lord[f.name1] = lord2
          lord_to_fellows[lord2].add(f.name1)
      else:
        if lord1 == lord2:
          pass
        else:
          fellows1 = lord_to_fellows[lord1]
          fellows2 = lord_to_fellows[lord2]
          if len(fellows1) > len(fellows2):
            # 加入一群
            for fellow in fellows2:
              fellow_to_lord[fellow] = lord1
            lord_to_fellows[lord1].update(fellows2)
            # 二群解散
            del lord_to_fellows[lord2]
          else:
            # 加入二群
            for fellow in fellows1:
              fellow_to_lord[fellow] = lord2
            lord_to_fellows[lord2].update(fellows1)
            # 二群解散
            del lord_to_fellows[lord1]

    return len(lord_to_fellows)


def test_uf():
  fellowships = [
    Fellowship('张三', '李四'),
    Fellowship('李四', '王五'),
    Fellowship('赵六', '胡二'),
    Fellowship('田七', '胡八'),
    Fellowship('胡八', '赵六'),
    Fellowship('田七', '王五'),
    Fellowship('李想', '张进'),
    Fellowship('李想', '李雷'),
  ]
  s = Solution()
  assert s.findProvinceNum(fellowships) == 2
