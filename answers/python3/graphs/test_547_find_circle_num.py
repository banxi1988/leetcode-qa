# coding: utf-8

__author__ = '代码会说话'
"""
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2 
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：

N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。
"""

from typing import List, DefaultDict
from collections import defaultdict


class UF:

  def __init__(self):
    self.circle_to_friends: DefaultDict[int, set] = defaultdict(set)
    self.friend_to_lord: dict = {}

  def create_ifneeded(self, i):
    ilord = self.friend_to_lord.get(i)
    if ilord is None:
      self.friend_to_lord[i] = i
      self.circle_to_friends[i].add(i)

  def union(self, i: int, j: int):
    ilord = self.friend_to_lord.get(i)
    jlord = self.friend_to_lord.get(j)
    if ilord is None and jlord is None:
      lord = i
      self.circle_to_friends[lord].add(i)
      self.circle_to_friends[lord].add(j)
      self.friend_to_lord[i] = lord
      self.friend_to_lord[j] = lord
    elif ilord is not None and jlord is not None:
      if ilord == jlord:
        return
      ilord_friends = self.circle_to_friends[ilord]
      jlord_friends = self.circle_to_friends[jlord]
      if len(ilord_friends) > len(jlord_friends):
        for friend in jlord_friends:
          ilord_friends.add(friend)
          self.friend_to_lord[friend] = ilord
        del self.circle_to_friends[jlord]
      else:
        for friend in ilord_friends:
          jlord_friends.add(friend)
          self.friend_to_lord[friend] = jlord
        del self.circle_to_friends[ilord]
    else:
      if ilord is not None:
        self.friend_to_lord[j] = ilord
        self.circle_to_friends[ilord].add(j)
      else:
        self.friend_to_lord[i] = jlord
        self.circle_to_friends[jlord].add(i)


class Solution:
  def findCircleNum(self, M: List[List[int]]) -> int:
    uf = UF()
    N = len(M)
    for i in range(N):
      for j in range(i, N):
        if i == j:
          uf.create_ifneeded(i)
        else:
          if M[i][j] == 1:
            uf.union(i, j)
          else:
            uf.create_ifneeded(i)
            uf.create_ifneeded(j)

    return len(uf.circle_to_friends)


def test():
  s = Solution()

  assert s.findCircleNum([[1]]) == 1
  assert s.findCircleNum([[1, 0, 0, 1],
                          [0, 1, 1, 0],
                          [0, 1, 1, 1],
                          [1, 0, 1, 1]]) == 1

  assert s.findCircleNum([[1, 1, 0],
                          [1, 1, 1],
                          [0, 1, 1]]) == 1

  assert s.findCircleNum([[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]]) == 3

  assert s.findCircleNum([[1, 1, 0],
                          [1, 1, 0],
                          [0, 0, 1]]) == 2
