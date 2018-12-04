# coding: utf-8

__author__ = 'banxi'

"""
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


class TrieNode:
    def __init__(self,ch:str):
        self.ch = ch
        self.count = 0
        self.children = {} # type Dict[str,TrieNode]

    def insert(self, word:str):
        """插入一个单词"""
        parent = self
        for ch in word:
            node = parent.children.get(ch)
            if not node:
                node = TrieNode(ch)
                parent.children[ch] = node
            parent = node
        parent.count+=1


from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, words:List[str], k:int) -> List[str]:
        word_to_count = defaultdict(int)
        for word in words:
            word_to_count[word] += 1
        counts = sorted(set(word_to_count.values()),reverse=True)
        count_to_words = defaultdict(list)
        for word,count in word_to_count.items():
            count_to_words[count].append(word)
        total_count = 0
        freq_index = 0
        freq_words = []
        while total_count < k:
            count = counts[freq_index]
            tmp_words = count_to_words[count]
            words_count = len(tmp_words)
            if words_count > 1:
                tmp_words.sort()
            if total_count + words_count> k:
                nums = k -total_count
                freq_words.extend(tmp_words[:nums])
                total_count += nums
            else:
                freq_words.extend(tmp_words)
                total_count += words_count
            freq_index+=1
        return  freq_words





def test_top_k_frequent():
    s = Solution()
    assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],3) == ["i", "love","coding"]
    # assert s.topKFrequent(["i"],1) == ["i"]
    # assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2) == ["i", "love"]
    # assert s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4) == ["the", "is", "sunny", "day"]
