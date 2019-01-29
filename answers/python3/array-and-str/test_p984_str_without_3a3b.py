# coding: utf-8

__author__ = '代码会说话'
"""
给定两个整数 A 和 B，返回任意字符串 S，要求满足：

S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
子串 'aaa' 没有出现在 S 中；
子串 'bbb' 没有出现在 S 中。
 

示例 1：

输入：A = 1, B = 2
输出："abb"
解释："abb", "bab" 和 "bba" 都是正确答案。
示例 2：

输入：A = 4, B = 1
输出："aabaa"
 

提示：

0 <= A <= 100
0 <= B <= 100
对于给定的 A 和 B，保证存在满足要求的 S。


"""

def assert_result(s:str,A:int,B:int):
    assert len(s) == A + B
    assert s.count('a') == A
    assert s.count('b') == B
    assert s.find("aaa") == -1
    assert s.find("bbb") == -1


class Solution:
    def strWithout3a3b(self, A:int, B:int) -> str:
        if A == 0:
            return 'b' * B
        if B == 0:
            return  'a' * A
        result = ""
        a = A
        b = B
        while a or b:
          if len(result) > 1 and result[-1] == result[-2]:
              appendA = result[-1] == 'b'
          else:
              appendA = a >= b

          if appendA:
              result += 'a'
              a -= 1
          else:
              result += 'b'
              b -= 1

        assert_result(result, A,B)
        return result


def test():
    s = Solution()
    s.strWithout3a3b(6,6)
    s.strWithout3a3b(5,5)
    s.strWithout3a3b(4,7)
    s.strWithout3a3b(4,6)
    s.strWithout3a3b(4,5)
    s.strWithout3a3b(4,4)
    s.strWithout3a3b(1,1)
    s.strWithout3a3b(1,2)
    s.strWithout3a3b(1,3)
    s.strWithout3a3b(1,4)
    s.strWithout3a3b(2,6)
    s.strWithout3a3b(3,7)
    s.strWithout3a3b(3,8)

