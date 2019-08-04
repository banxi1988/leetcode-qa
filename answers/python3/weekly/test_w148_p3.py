# coding: utf-8

__author__ = '代码会说话'

"""
实现支持下列接口的「快照数组」- SnapshotArray：

SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
 

示例：

输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
 

提示：

1 <= length <= 50000
题目最多进行50000 次set，snap，和 get的调用 。
0 <= index < length
0 <= snap_id < 我们调用 snap() 的总次数
0 <= val <= 10^9
"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter

class Snap:
  def __init__(self):
    self.data = {}
    self.effective_snap_id = -1

  def set(self,val:int):
    self.data[-1] = val

  def snap(self,snap_id:int):
    val = self.data.get(-1)
    if val is not None:
      self.data[snap_id] = val
      self.last_changed_snap_id = snap_id

  def get(self,snap_id:int):
    esid = self.effective_snap_id
    if esid != -1 and  snap_id >= esid:
      return self.data[esid]
    else:
      return self.data.get(snap_id, 0)

class SnapshotArray:

  def __init__(self, length: int):
    self._snap_id = -1
    self.length = length
    self.index_to_snap = defaultdict(Snap)

  def set(self, index: int, val: int) -> None:
    snap = self.index_to_snap[index]
    snap.set(val)

  def snap(self) -> int:
    self._snap_id += 1
    snap_id = self._snap_id
    for index,snap in self.index_to_snap.items():
      snap.snap(snap_id)
    return snap_id

  def get(self, index: int, snap_id: int) -> int:
    snap = self.index_to_snap[index]
    return snap.get(snap_id)


# Your SnapshotArray object will be instantiated and called as such:


def test():
   obj = SnapshotArray(3)
   obj.set(0,5)
   assert obj.snap() == 0
   obj.set(0,6)
   assert obj.get(0,0) == 5
   assert obj.snap() == 1
   assert obj.get(0,1) == 6

   assert obj.get(2,1) == 0

   sa2 = SnapshotArray(1)
   sa2.set(0,15)
   assert sa2.snap() == 0
   assert sa2.snap() == 1
   assert sa2.snap() == 2
   sa2.get(0,15)
   assert sa2.snap() == 3
   assert sa2.snap() == 4
   sa2.set(0,15)


