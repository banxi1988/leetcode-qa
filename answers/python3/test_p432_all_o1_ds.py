# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 432. 全 O(1) 的数据结构双向链表+哈希算法详解 by 代码会说话
实现一个数据结构支持以下操作：

Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否者使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串""。
GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。

挑战：以 O(1) 的时间复杂度实现所有操作。
"""

class KeyValue:
  """ 双向链接表的节点数据结构  """
  def __init__(self,key:str):
    self.key = key
    self.value = 1
    self.next = None # type: KeyValue
    self.prev = None # type: KeyValue

class AllOne:

  def __init__(self):
    # 3,2,1
    self.head = None # type: KeyValue
    self.last = None # type: KeyValue
    self.key_to_keyvalue = {}
    # 3,2
    # 3,2,1

  def deleteKeyValue(self,kv:KeyValue):
    """删除链表节点"""
    is_head = kv.prev is None
    is_last = kv.next is None
    prev = kv.prev
    next = kv.next
    if is_last and is_head:
      self.head = None
      self.last = None
    elif is_head:
      self.head = next
      self.head.prev = None
    elif is_last:
      prev.next = None
      self.last = prev
    else:
      prev.next = next
      next.prev = prev

  def append(self,kv:KeyValue):
    if self.last:
      self.last.next = kv
      kv.prev = self.last
      self.last = kv
    else:
      self.head = kv
      self.last = kv

  def insertHead(self, kv:KeyValue):
    if self.head is None:
      return self.append(kv)
    # [3] 2
    kv.next = self.head
    self.head.prev = kv
    self.head = kv
    kv.prev = None

  def insertAfter(self,p:KeyValue,kv:KeyValue):
    # 3
    p_next = p.next
    if p_next is None:
      return self.append(kv)
    kv.next = p_next
    p_next.prev = kv
    p.next = kv
    kv.prev = p

  def insertBefore(self, p:KeyValue,kv:KeyValue):
    # 3,1
    p_prev = p.prev
    if p_prev is None:
      self.insertHead(kv)
    else:
      self.insertAfter(p_prev, kv)


  def inc(self, key:str):
    # O(1)
    kv = self.key_to_keyvalue.get(key) # type: KeyValue
    if kv is None:
      kv = KeyValue(key)
      self.key_to_keyvalue[key] = kv
      return self.append(kv)
    kv.value += 1
    # 2,2,2,2,1,2
    prev = kv.prev
    if not prev:
      return
    # 向左走
    self.deleteKeyValue(kv)
    while prev:
      if prev.value < kv.value:
        prev = prev.prev
      else:
        break
    if prev:
      self.insertAfter(prev, kv)
    else:
      self.insertHead(kv)

  def dec(self, key:str):
    kv = self.key_to_keyvalue.get(key) # type: KeyValue
    if kv is None:
      return
    kv.value -=1
    if kv.value == 0:
      del self.key_to_keyvalue[key]
      self.deleteKeyValue(kv)
      return
    # 4,3,1,2,2,1
    next = kv.next
    if next is None:
      return
    # 向右走
    self.deleteKeyValue(kv)
    while next:
      if next.value > kv.value:
        next = next.next
      else:
        break
    if next is None:
      self.append(kv)
    else:
      self.insertBefore(next,kv)

  def getMaxKey(self):
    if self.head:
      return self.head.key
    return  ""

  def getMinKey(self):
    if self.last:
      return  self.last.key
    return  ""

def test():
  # 测试用例1
  a1 = AllOne()
  a1.inc("a")
  a1.inc("b")
  a1.inc("b")
  a1.inc("c")
  a1.inc("c")
  a1.inc("c")
  a1.dec("b")
  a1.dec("b")
  assert a1.getMinKey() == "a"
  a1.dec("a")
  assert a1.getMinKey() == "c"
  assert a1.getMaxKey() == "c"

  # 测试用例2
  a2 = AllOne()
  a2.inc("san")
  assert a2.getMaxKey() == "san";
  assert a2.getMinKey() == "san";
  a2.inc("san")
  a2.inc("yan")
  assert a2.getMaxKey() == "san";
  assert a2.getMinKey() == "yan";
  a2.dec("yan")
  assert a2.getMaxKey() == "san";
  assert a2.getMinKey() == "san";

  # 测试用例3
  a3 = AllOne()
  a3.inc("san")
  a3.dec("san")
  assert a3.getMaxKey() == "";
  assert a3.getMinKey() == "";

  # 测试用例4
  a4 = AllOne()
  a4.inc("hello")
  a4.inc("goodbye")
  a4.inc("hello")
  a4.inc("hello")
  assert a4.getMaxKey() == "hello"
  a4.inc("leet")
  a4.inc("code")
  a4.inc("leet")
  a4.dec("hello")
  a4.inc("leet")
  a4.inc("code")
  a4.inc("code")
  assert a4.getMaxKey() == "leet"

  # 测试用例5
  a5 = AllOne()
  a5.inc("hello")
  a5.inc("hello")
  a5.inc("world")
  a5.inc("world")
  a5.inc("hello")
  a5.dec("world")
  assert a5.getMaxKey() == "hello"
  assert a5.getMinKey() == "world"



