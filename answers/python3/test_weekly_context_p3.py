# coding: utf-8
"""
给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

示例 1：

输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
输出：4
示例 2：

输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
输出：2
"""


class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        x_to_points = defaultdict(list)
        y_to_points = defaultdict(list)
        for point in points:
            x, y = point
            x_to_points[x].append(point)
            y_to_points[x].append(point)
        y_to_hlines = defaultdict(list)
        for (y, points) in y_to_points.items():
            xlist = [p[0] for p in points]
            xlist.sort()


def test_wc110_p3():
    solution = Solution()
    input1 = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    assert solution.minAreaRect(input1) == 4

    input2 = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
    assert solution.minAreaRect(input2) == 2


"""
参考答案 from uwi
class Solution {
	    public int minAreaRect(int[][] points) {
	        int n = points.length;
	        Set<Long> set = new HashSet<>();
	        for(int i = 0;i < n;i++){
	        	set.add((long)points[i][0]<<32|points[i][1]);
	        }
	        
	        int ret = Integer.MAX_VALUE;
	        for(int i = 0;i < n;i++){
	        	for(int j = i+1;j < n;j++){
	        		long S = Math.abs((long)(points[i][0]-points[j][0])*(points[i][1]-points[j][1]));
	        		if(S == 0)continue;
	        		long x = (long)points[i][0]<<32|points[j][1];
	        		if(!set.contains(x))continue;
	        		x = (long)points[j][0]<<32|points[i][1];
	        		if(!set.contains(x))continue;
	        		ret = Math.min(ret, (int)S);
	        	}
	        }
	        if(ret == Integer.MAX_VALUE)return 0;
	        return ret;
	    }
	}	

"""
