# coding: utf-8
from typing import NamedTuple, DefaultDict

__author__ = '代码会说话'

"""
并查集介绍及应用 (1)
创建同乡群

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
  assert len(provinces) == 2


class Fellowship(NamedTuple):
  """同乡关系"""
  name1: str
  name2: str


from collections import defaultdict
from typing import List


class FellowshipUnionFind:
  fellow_to_lord: dict = {}  # 同乡-> 群主
  lord_to_fellows: DefaultDict = defaultdict(set)

  def union(self, ship: Fellowship):
    fellow_to_lord = self.fellow_to_lord
    lord_to_fellows = self.lord_to_fellows
    lord1 = fellow_to_lord.get(ship.name1)
    lord2 = fellow_to_lord.get(ship.name2)
    if lord1 is None and lord2 is None:
      # 说明两个人都没有在任何一个同乡群了
      lord = ship.name1
      fellow_to_lord[ship.name1] = lord
      fellow_to_lord[ship.name2] = lord

      lord_to_fellows[lord].add(ship.name1)
      lord_to_fellows[lord].add(ship.name2)
    elif lord1 and lord2:
      # 说明两个人都在某一个同乡群了
      if lord1 == lord2:
        pass
      else:
        fellows1 = lord_to_fellows[lord1]
        fellows2 = lord_to_fellows[lord2]
        if len(fellows1) > len(fellows2):
          target_lord = lord1
          discard_lord = lord2
          new_fellows = fellows2
        else:
          target_lord = lord2
          discard_lord = lord1
          new_fellows = fellows1

        for fellow in new_fellows:
          fellow_to_lord[fellow] = target_lord
          lord_to_fellows[target_lord].add(fellow)
        del lord_to_fellows[discard_lord]

    else:
      # 说明两个人中有一个已经在某一个同乡群了
      if lord1:
        fellow_to_lord[ship.name2] = lord1
        lord_to_fellows[lord1].add(ship.name2)
      else:
        fellow_to_lord[ship.name1] = lord2
        lord_to_fellows[lord2].add(ship.name1)

  def find_biggest_lord(self, name: str):
    lord = self.fellow_to_lord.get(name)
    prev_lord = lord
    while lord:
      prev_lord = lord
      lord = self.fellow_to_lord.get(lord)
    return prev_lord

  def has_fellow_ship(self, name1: str, name2: str):
    lord1 = self.find_biggest_lord(name1)
    # lord1 -> lord_parent -> lord_parent
    lord2 = self.find_biggest_lord(name2)
    return lord1 == lord2


class Solution:
  """
  群主: lord
  同乡: fellow
  """
  def findProvinceNum(self, fellowships: List[Fellowship]) -> int:
    uf = FellowshipUnionFind()
    for ship in fellowships:
      uf.union(ship)
    return len(uf.lord_to_fellows)


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
