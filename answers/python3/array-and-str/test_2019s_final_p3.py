# coding: utf-8

__author__ = '代码会说话'

"""
给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。

 

示例 1：

输入："abcd"
输出：0
解释：没有重复子串。
示例 2：

输入："abbaba"
输出：2
解释：最长的重复子串为 "ab" 和 "ba"，每个出现 2 次。
示例 3：

输入："aabcaabdaab"
输出：3
解释：最长的重复子串为 "aab"，出现 3 次。
示例 4：

输入："aaaaa"
输出：4
解释：最长的重复子串为 "aaaa"，出现 2 次。
 

提示：

字符串 S 仅包含从 'a' 到 'z' 的小写英文字母。
1 <= S.length <= 1500
"""


class Solution:
  def longestRepeatingSubstring(self, S: str) -> int:
    N = len(S)
    maxl = 1
    start = 0
    found = False
    while maxl < N:
      found = False
      for i in range(start, N - maxl):
        s1 = S[i:i + maxl]
        others = S[i + 1:]
        if s1 in others:
          found = True
          start = i
          break
      if not found:
        return maxl - 1
      maxl += 1
    if found:
      return maxl - 1
    return 0

  def longestRepeatingSubstring_old(self, S: str) -> int:
    N = len(S)
    maxl = N - 1
    while maxl > 0:
      for i in range(0, N - maxl):
        s1 = S[i:i + maxl]
        others = S[i + 1:]
        if s1 in others:
          return maxl
      maxl -= 1
    return 0


def test():
  s = Solution()
  assert s.longestRepeatingSubstring("abbaba") == 2
  assert s.longestRepeatingSubstring("aaaaa") == 4
  assert s.longestRepeatingSubstring("abcd") == 0
  assert s.longestRepeatingSubstring("aaaa") == 3
  assert s.longestRepeatingSubstring("aaa") == 2
  assert s.longestRepeatingSubstring("aa") == 1

  larges = "gymjkqexonleccucwuofmuirwtdvjescmjvdulychgavmbbgcluxbjrewurytkwxnpvgssttlcbrwysncyqxxmpajrgibnihjxchtsnwcwsmhndomnthvlehuynimnskqgeqbtyvcecdjrjtkuamswamunxhwlmiorxtlkogxetsuhijesobgsoylxqpmrolkhwywyktxthrhgiejavdjsxhhriamvegqeghmvbqxyetptucgtfmfjobqbunlxsoehkysdnqsxtdyjlrwifvytfgpsycaanqeusuluwyuclvybgnajospbhtjgfwujxorrtpnvcquecatqhvlitibjtclhqxjwjybggucayaifoidjupjixudfnehiuflscvejxvytsxobriympthgbtyllhcrfyblylsqrcmjvpatixxlgxlmftuildsukpiuvqnkkgblohmnbktdvqoaixxnmntjkjamodnkownuyypipmmtdcbxgxjkwsjlyehothcnkbtoyeyhclmpfygmtpvpyggbyjsbqpbidvrvukwdbconiuqcetidiwuxldmcufxjqpdnuwjyfcfbjxvwsboqnbeghsulsjiceavpqeeixjgekgkppgqominhvsdfelxgjbapkhqfuyrdcugcphejatwnlcbgthirvwuhnecragftulfgkyvtrdnuycbpetoucrktynkdixnuxjwrsopofmkwclmtxexbkgywymsfphmvxcenhancsyeiwuqtewjvdvybfxjlppftktcwyphsyknhbucytepbokkvvhyklpuglhgcuonovhtdgifoxkqqvjnqctatdkeqaueygdptllxswgrrebmhrdedhhpnftmadskejjjwpvkfubonuoscyxkccsnskclfqfnjwgtmuxmttowolhxiwojhqnasxkikmpiolnqlvfroyvajjcqambwtfholxtnwfuylvnycoinulwargrikogjubn"

  assert s.longestRepeatingSubstring(larges) == 4
