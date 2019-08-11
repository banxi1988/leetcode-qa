# coding: utf-8

__author__ = '代码会说话'

"""
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。

 

示例 1：

输入：text = "ababa"
输出：3
示例 2：

输入：text = "aaabaaa"
输出：6
示例 3：

输入：text = "aaabbaaa"
输出：4
示例 4：

输入：text = "aaaaa"
输出：5
示例 5：

输入：text = "abcdef"
输出：1
 

提示：

1 <= text.length <= 20000
text 仅由小写英文字母组成。
"""

from typing import List, NamedTuple
from collections import defaultdict

class ChCnt(NamedTuple):
  ch:str
  cnt:int

class Solution:
  def maxRepOpt1(self, text: str) -> int:
    prev_ch = text[0]
    prev_ch_cnt = 1
    pairs = []
    for ch in text[1:]:
      if ch == prev_ch:
        prev_ch_cnt += 1
      else:
        pairs.append(ChCnt(prev_ch,prev_ch_cnt))
        prev_ch = ch
        prev_ch_cnt = 1
    pairs.append(ChCnt(prev_ch,prev_ch_cnt))
    ch_to_pair_index_set = defaultdict(set)
    for index,pair in enumerate(pairs):
      ch_to_pair_index_set[pair.ch].add(index)

    N = len(pairs)
    max_len = 1
    for i in range(N):
      pair = pairs[i]
      if pair.cnt > max_len:
        max_len = pair.cnt
      j = i+1
      k = i+2
      if k < N:
        pairj = pairs[j]
        pairk = pairs[k]
        if pairk.ch == pair.ch:
          index_set = set(ch_to_pair_index_set[pair.ch])
          index_set.discard(i)
          index_set.discard(k)
          if pairj.cnt == 1:
            cur_len = pair.cnt + pairk.cnt
            if len(index_set) > 0:
              cur_len += 1
          else:
            cur_len = max(pair.cnt, pairk.cnt) + 1
          if cur_len > max_len:
            max_len = cur_len
    return max_len






def test():
  s = Solution()
  assert s.maxRepOpt1(text = "ababa") == 3
  assert s.maxRepOpt1(text = "abbaba") == 3
  assert s.maxRepOpt1(text = "abbabba") == 4
  assert s.maxRepOpt1(text = "aaabaaa") == 6
  assert s.maxRepOpt1(text = "aaabbaaa") == 4
  assert s.maxRepOpt1(text = "aaaaa") == 5
  assert s.maxRepOpt1(text = "abcdef") == 1
