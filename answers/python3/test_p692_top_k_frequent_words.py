# coding: utf-8

__author__ = 'banxi'

"""
LeetCode 692. 前K个高频单词 @by 代码会说话

给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
 

示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 

注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。
"""


from typing import List
from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, words:List[str], k:int) -> List[str]:
        """
        select word,count(word) as cnt from words
        group by word
        order by cnt desc,word asc
        limit 3
        """
        # i: 2
        # love: 2
        word_to_count = Counter(words)
        freq_words = sorted(word_to_count.keys(),key=lambda word:(-word_to_count[word],word))
        return freq_words[:k]










def test_top_k_frequent():
    s = Solution()
    assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],3) == ["i", "love","coding"]
    assert s.topKFrequent(["i"],1) == ["i"]
    assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2) == ["i", "love"]
    assert s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4) == ["the", "is", "sunny", "day"]
