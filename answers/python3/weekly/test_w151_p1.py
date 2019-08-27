# coding: utf-8

__author__ = '代码会说话'

"""
如果出现下述两种情况，交易 可能无效：

交易金额超过 ¥1000
或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）
每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。

给你一份交易清单 transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。

 

示例 1：

输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
输出：["alice,20,800,mtv","alice,50,100,beijing"]
解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。
示例 2：

输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
输出：["alice,50,1200,mtv"]
示例 3：

输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
输出：["bob,50,1200,mtv"]
 

提示：

transactions.length <= 1000
每笔交易 transactions[i] 按 "{name},{time},{amount},{city}" 的格式进行记录
每个交易名称 {name} 和城市 {city} 都由小写英文字母组成，长度在 1 到 10 之间
每个交易时间 {time} 由一些数字组成，表示一个 0 到 1000 之间的整数
每笔交易金额 {amount} 由一些数字组成，表示一个 0 到 2000 之间的整数
"""

from typing import List, NamedTuple
from functools import lru_cache
from collections import defaultdict, Counter

class Tx(NamedTuple):
  no:int
  name:str
  time:int
  amount:int
  city:int

class Solution:
  def invalidTransactions(self, transactions: List[str]) -> List[str]:
    txs: List[Tx] = []
    for no,t in enumerate(transactions):
      name,time,amount,city = t.split(',')
      tx = Tx(no,name,int(time),int(amount),city)
      txs.append(tx)

    name_to_txs = defaultdict(list)
    for tx in txs:
      name_to_txs[tx.name].append(tx)
    invalid_nos = set()
    for name,txs in name_to_txs.items():
      txs.sort(key=lambda t: t.time)
      for tx in txs:
        if tx.amount > 1000:
          invalid_nos.add(tx.no)
        near_txs = []
        for otx in txs:
          if otx.no == tx.no:
            continue
          if abs(otx.time - tx.time) <= 60:
            near_txs.append(otx)
        for ntx in near_txs:
          if ntx.city != tx.city:
            invalid_nos.add(ntx.no)
            invalid_nos.add(tx.no)

    invalid_tx = []
    for i in invalid_nos:
      invalid_tx.append(transactions[i])

    return invalid_tx




def test():
  s = Solution()
  assert s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]) == ["alice,20,800,mtv","alice,50,100,beijing"]

  assert s.invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]) == ["bob,50,1200,mtv"]

  assert s.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]) == ["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]
