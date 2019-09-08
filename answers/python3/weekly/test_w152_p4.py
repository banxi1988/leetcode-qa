# coding: utf-8

__author__ = '代码会说话'

"""
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。

字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：

单词 word 中包含谜面 puzzle 的第一个字母。
单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

 

示例：

输入：
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
 

提示：

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] 都是小写英文字母。
每个 puzzles[i] 所包含的字符都不重复。
"""

from typing import List
from collections import defaultdict

class Solution:
  def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
    ch_to_bit = [0] * 26
    for i in range(0,26):
      bit = 1 << i
      ch_to_bit[i] = bit

    word_bits_to_cnt = defaultdict(int)
    ord_a = ord('a')
    for i,word in enumerate(words):
      bits = 0
      for ch in word:
        chi = ord(ch) - ord_a
        bits |= ch_to_bit[chi]
      word_bits_to_cnt[bits] += 1
    ans = [0] * (len(puzzles))
    for i,puzzle in enumerate(puzzles):
      bits = 0
      for ch in puzzle:
        chi = ord(ch) - ord_a
        bits |= ch_to_bit[chi]
      first_bit = ch_to_bit[ord(puzzle[0]) - ord_a]
      wbits = bits
      cnt = 0
      while wbits > 0:
        if first_bit & wbits == first_bit:
          cnt += word_bits_to_cnt.get(wbits,0)
        wbits = (wbits -1) & bits
      ans[i] = cnt

    return ans


from weekly import w152_p4


def test():
  s = Solution()
  assert s.findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"],
                               puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]) == [1,1,3,2,4,0]

  assert s.findNumOfValidWords(words=w152_p4.words,puzzles=w152_p4.puzzles)
