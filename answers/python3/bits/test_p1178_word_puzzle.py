# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 1178]. 猜字谜(难度:困难)

外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。

字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：

单词 word 中包含谜面 puzzle 的第一个字母。
单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

 

示例：

输入：
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
words = ["aaaa","asas","able","ability","actt","actor","access"], 
['a','as','able','abilty']

'a': 1
'b': 10
'c': 100
'd': 1000

ab: 1 | 10 = 11
aab: 1 | 1 | 10 = 11
ac: 101
abc: 111
ad,da: 1001

adc: 1101
ab:    11

1101 & 0011 = 01 != 11





[1][2][3]...[26]
 a b  c      z
 

log2N

# M*N*L*PL

提示：

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] 都是小写英文字母。
每个 puzzles[i] 所包含的字符都不重复。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import defaultdict


class Solution:
  def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
    ch_to_bit = {}
    ord_a = ord('a')
    for i in range(0,26):
      bit = 1 << i
      ch = chr(ord_a + i)
      ch_to_bit[ch] = bit

    word_bits_to_count = defaultdict(int)
    for word in words:
      bits = 0
      for ch in word:
        bit = ch_to_bit[ch]
        bits |= bit
      word_bits_to_count[bits] += 1

    ans = [0]*(len(puzzles))
    for i,puzzle in enumerate(puzzles):
      puzzle_bits = 0
      for ch in puzzle:
        bit = ch_to_bit[ch]
        puzzle_bits |= bit

      total_cnt = 0
      first_bit = ch_to_bit[puzzle[0]]
      # 26 位
      # 8 7
      # 8: 1000
      # 7: 0111     0

      # 6: 0110
      # 5: 0101
      cur_bits = puzzle_bits
      while cur_bits > 0:
        if (cur_bits & first_bit) == first_bit:
          cnt = word_bits_to_count.get(cur_bits,0)
          total_cnt += cnt
        cur_bits -= 1
        cur_bits = cur_bits & puzzle_bits



      # for word_bits,cnt in word_bits_to_count.items():
      #   if (word_bits & first_bit) != first_bit:
      #     continue
      #   if (puzzle_bits & word_bits) == word_bits:
      #     total_cnt += cnt


      ans[i] = total_cnt
    return ans







def test():
  s = Solution()
  assert s.findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"],
                               puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]) == [1,1,3,2,4,0]
