# coding: utf-8

__author__ = '代码会说话'


class Solution:
  def removeOuterParentheses(self, S: str) -> str:
    results = []
    depth = 0
    p_group = []
    for ch in S:
      if ch == ')':
        depth -= 1
        if depth == 0:
          # no need append
          t1 = ''.join(p_group[1:])
          results.append(t1)
          p_group = []
        else:
          p_group.append(ch)
      else:
        depth += 1
        p_group.append(ch)

    return ''.join(results)


def test():
  s = Solution()
  assert s.removeOuterParentheses("(()())(())") == "()()()"
  assert s.removeOuterParentheses("(()())((()))") == "()()(())"
  assert s.removeOuterParentheses( "(()())(())(()(()))")== "()()()()(())"
  assert s.removeOuterParentheses("()()") == ""
  assert s.removeOuterParentheses("(())") == "()"
