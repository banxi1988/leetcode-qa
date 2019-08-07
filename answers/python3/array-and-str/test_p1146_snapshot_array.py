# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 1146]. 快照数组(难度: 中等, 分值: 6分)

实现支持下列接口的「快照数组」- SnapshotArray：

SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
 

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
snapshotArr.snap() // snap_id = 1
snapshotArr.get(0,1) // 6

[0] = {
  0: 5,
  1: 6,
  3: 3
  snap_ids: [0,1,3]
}

提示：

1 <= length <= 50000
题目最多进行50000 次set，snap，和 get的调用 。
0 <= index < length
0 <= snap_id < 我们调用 snap() 的总次数
0 <= val <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/snapshot-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import defaultdict
import bisect

class Snap:
  def __init__(self):
    self.data = {}
    self.snap_ids = []

  def set(self,val:int):
    self.data[-1] = val

  def snap(self,snap_id:int):
    val = self.data.get(-1)
    if val is not None:
      self.data[snap_id] = val
      self.snap_ids.append(snap_id)
      del self.data[-1]


  def get(self,snap_id):
    val = self.data.get(snap_id)
    if val is not None:
      return val
    index = bisect.bisect_left(self.snap_ids, snap_id) -1
    if index >= 0:
      last_changed_snap_id = self.snap_ids[index]
      return self.data.get(last_changed_snap_id,0)
    return 0


class SnapshotArray:

  def __init__(self, length: int):
    self.index_to_snap = defaultdict(Snap)
    self.snap_id = -1

  def set(self, index: int, val: int) -> None:
    self.index_to_snap[index].set(val)

  def snap(self) -> int:
    self.snap_id += 1
    snap_id = self.snap_id
    for snap in self.index_to_snap.values():
      snap.snap(snap_id)
    return self.snap_id

  def get(self, index: int, snap_id: int) -> int:
    return self.index_to_snap[index].get(snap_id)





def test():
  obj = SnapshotArray(3)
  obj.set(0, 5)
  assert obj.get(0,0) == 0
  snap_id =  obj.snap()
  assert snap_id == 0
  obj.set(0, 6)
  assert obj.get(0, 0) == 5
  assert obj.get(1, 0) == 0

  assert obj.snap() == 1
  assert obj.snap() == 2
  assert obj.get(0, 2) == 6
  obj.set(0, 4)
  obj.set(0, 3)
  assert obj.get(0,1) == 6
  assert obj.get(0,2) == 6
  assert obj.get(0,0) == 5
  assert obj.snap() == 3
  assert obj.get(0,3) == 3
  obj.snap()
  obj.snap()

  assert obj.get(0,3) == 3
  assert obj.get(0,2) == 6

