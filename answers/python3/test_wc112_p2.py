#coding: utf-8


class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        popped.reverse()
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and popped and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()

        return  len(popped) == 0



def test():
    s = Solution()

    # assert s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) == True
    # assert s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) == False
    assert s.validateStackSequences([1,2,3], [1,3,2]) == True
    # assert s.validateStackSequences([1,2,3], [1,2,3]) == True
    # assert s.validateStackSequences([3,2,1], [1,2,3]) == True
