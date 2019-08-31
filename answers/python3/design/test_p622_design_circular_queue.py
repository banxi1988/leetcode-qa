# coding: utf-8
from collections import deque

__author__ = '代码会说话'

"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
 

示例：

MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3

circularQueue.enQueue(1);  // 返回 true

circularQueue.enQueue(2);  // 返回 true

circularQueue.enQueue(3);  // 返回 true

circularQueue.enQueue(4);  // 返回 false，队列已满

circularQueue.Rear();  // 返回 3

circularQueue.isFull();  // 返回 true

circularQueue.deQueue();  // 返回 true

circularQueue.enQueue(4);  // 返回 true

circularQueue.Rear();  // 返回 4
 
 

提示：

所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-circular-queue
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MyCircularQueue:

  def __init__(self, k: int):
    self.dq = deque()
    self.k = k

  def enQueue(self, value: int) -> bool:
    """插入一个元素进队列,成功返回True """
    if self.isFull():
      return False
    self.dq.append(value)
    return True

  def deQueue(self) -> bool:
    """从队列删除一个元素,成功返回 True """
    if not self.isEmpty():
      self.dq.popleft()
      return True
    else:
      return False

  def Front(self) -> int:
    """返回列头第一个元素"""
    if self.isEmpty():
      return -1
    return self.dq[0]

  def Rear(self) -> int:
    """返回列尾最后一个元素 """
    if self.isEmpty():
      return -1
    return self.dq[-1]

  def isEmpty(self) -> bool:
    """判断队列是否为空 """
    return len(self.dq) == 0

  def isFull(self) -> bool:
    """判断队列是否已满 """
    return len(self.dq) == self.k

def test():
  circularQueue = MyCircularQueue(3)
  assert circularQueue.enQueue(1)

  assert circularQueue.enQueue(2)
  assert circularQueue.enQueue(3)
  assert not circularQueue.enQueue(4)
  assert circularQueue.Rear() == 3
  assert circularQueue.isFull()
  assert circularQueue.deQueue()
  assert circularQueue.enQueue(4)
  assert circularQueue.Rear() == 4


  # ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
  # [[8],[3],[9],[5],[0],[],[],[],[],[],[],[]]
  # [null,true,true,true,true,true,true,false,false,0,0,true]
  q2 = MyCircularQueue(8)
  assert q2.enQueue(3)
  assert q2.enQueue(9)
  assert q2.enQueue(5)
  assert q2.enQueue(0)
  assert q2.deQueue()
  assert q2.deQueue()
  assert not q2.isEmpty()
  assert not q2.isEmpty()
  assert q2.Rear() == 0
  assert q2.Rear() == 0
  assert q2.deQueue()
