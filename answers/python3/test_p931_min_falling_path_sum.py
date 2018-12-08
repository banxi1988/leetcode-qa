# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 931. 下降路径最小和 题解 by 代码会说话

给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

 

示例：

输入：[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
输出：12
解释：
可能的下降路径有：
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
和最小的下降路径是 [1,4,7]，所以答案是 12。

 

提示：

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100

        [51,24],  [1,-26]
        [-50,82]  

"""

from typing import List

class Solution:
    def minFallingPathSum(self, A:List[List[int]]) -> int:
        row_count = len(A)
        col_count = len(A[0])
        cur_row_path_sum = A[-1]
        MAX_NUM = 100 * 100 + 1
        for i in reversed(range(0,row_count-1)):
            row = A[i]
            next_row_path_sum = row
            for index,num in enumerate(row):
                midNum = cur_row_path_sum[index]
                leftNum = MAX_NUM
                rightNum = MAX_NUM
                if index > 0:
                    leftNum = cur_row_path_sum[index -1]
                if index < (col_count -1):
                    rightNum = cur_row_path_sum[index + 1]
                next_row_path_sum[index] += min(leftNum,midNum, rightNum)
            cur_row_path_sum = next_row_path_sum

        return min(cur_row_path_sum)





def test():
    s = Solution()

    rect1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    assert s.minFallingPathSum(rect1) == 12

    rect2 = [
        [51,24],
        [-50,82]
    ]
    assert s.minFallingPathSum(rect2) == -26

    rect3_1 = [
        [51,24]
    ]
    assert s.minFallingPathSum(rect3_1) == 24
    rect3_2 = [
        [1]
    ]
    assert s.minFallingPathSum(rect3_2) == 1

    rect4 = [[-19,-1,-96,48,-94,36,16,55,-42,37,-59,6,-32,96,95,-58,13,-34,94,85],[17,44,36,-29,84,80,-34,50,-99,64,13,91,-27,25,-36,57,20,98,-100,-72],[-92,-75,86,90,-4,90,64,56,50,-63,10,-15,90,-66,-66,32,-69,-78,1,60],[21,51,-47,-43,-14,99,44,90,8,11,99,-62,57,59,69,50,-69,32,85,13],[-28,90,12,-18,23,61,-55,-97,6,89,36,26,26,-1,46,-50,79,-45,89,86],[-85,-10,49,-10,2,62,41,92,-67,85,86,27,89,-50,77,55,22,-82,-94,-98],[-50,53,-23,55,25,-22,76,-93,-7,66,-75,42,-35,-96,-5,4,-92,13,-31,-100],[-62,-78,8,-92,86,69,90,-37,81,97,53,-45,34,19,-19,-39,-88,-75,-74,-4],[29,53,-91,65,-92,11,49,26,90,-31,17,-84,12,63,-60,-48,40,-49,-48,88],[100,-69,80,11,-93,17,28,-94,52,64,-86,30,-9,-53,-8,-68,-33,31,-5,11],[9,64,-31,63,-84,-15,-30,-10,67,2,98,73,-77,-37,-96,47,-97,78,-62,-17],[-88,-38,-22,-90,54,42,-29,67,-85,-90,-29,81,52,35,13,61,-18,-94,61,-62],[-23,-29,-76,-30,-65,23,31,-98,-9,11,75,-1,-84,-90,73,58,72,-48,30,-81],[66,-33,91,-6,-94,82,25,-43,-93,-25,-69,10,-71,-65,85,28,-52,76,25,90],[-3,78,36,-92,-52,-44,-66,-53,-55,76,-7,76,-73,13,-98,86,-99,-22,61,100],[-97,65,2,-93,56,-78,22,56,35,-24,-95,-13,83,-34,-51,-73,2,7,-86,-19],[32,94,-14,-13,-6,-55,-21,29,-21,16,67,100,77,-26,-96,22,-5,-53,-92,-36],[60,93,-79,76,-91,43,-95,-16,74,-21,85,43,21,-68,-32,-18,18,100,-43,1],[87,-31,26,53,26,51,-61,92,-65,17,-41,27,-42,-14,37,-46,46,-31,-74,23],[-67,-14,-20,-85,42,36,56,9,11,-66,-59,-55,5,64,-29,77,47,44,-33,-77]]
    assert s.minFallingPathSum(rect4) == -1428
