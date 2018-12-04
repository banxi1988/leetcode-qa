# coding: utf-8


"""
LeetCode 208 题解 By @代码会说话 （欢迎关注抖音账号）
实现一个 Trie (前缀树)
包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""

class TrieNode:
    def __init__(self,ch:str):
        self.ch = ch
        self.is_word = False
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
        parent.is_word = True

    def search(self, word:str) -> bool:
        """搜索单词是否在字典树中"""
        parent = self
        for ch in word:
            parent = parent.children.get(ch)
            if not parent:
                return False
        return parent.is_word


    def startsWith(self, prefix:str) -> bool:
        """此单词树中是否包含有对应前缀的单词 """
        parent = self
        for ch in prefix:
            parent = parent.children.get(ch)
            if not parent:
                return False
        return True


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word:str):
        """插入一个单词"""
        self.root.insert(word)

    def search(self, word:str) -> bool:
        """搜索单词是否在字典树中"""
        return self.root.search(word)

    def startsWith(self, prefix:str) -> bool:
        """此单词树中是否包含有对应前缀的单词 """
        return self.root.startsWith(prefix)


def test_trie():
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app") # is_word
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
    assert not trie.search('a')
    trie.insert('a')
    assert trie.search('a')
