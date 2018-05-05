Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

## 解题思路：
首先分析可重复组成的字符串的特点。
aa -> a|a
abab -> ab|ab
abcabc -> abc|abc

如果是有一个指定长度的 pattern 那么，我们就可以方便判断了。
所以在不知道 pattern 长度的时候，我们可以尝试从1到 n 的长度当作 pattern 长度来判断。

