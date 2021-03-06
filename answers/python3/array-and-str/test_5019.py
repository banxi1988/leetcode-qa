# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 5019. 视频拼接[6分题]

你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。

我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

 

示例 1：

输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
输出：3
解释：
我们选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]。
示例 2：

输入：clips = [[0,1],[1,2]], T = 5
输出：-1
解释：
我们无法只用 [0,1] 和 [0,2] 覆盖 [0,5] 的整个过程。
示例 3：

输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
输出：3
解释： 
我们选取片段 [0,4], [4,7] 和 [6,9] 。
示例 4：

输入：clips = [[0,4],[2,8]], T = 5
输出：2
解释：
注意，你可能录制超过比赛结束时间的视频。
 

提示：

1 <= clips.length <= 100
0 <= clips[i][0], clips[i][1] <= 100
0 <= T <= 100

输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
输出：3

[0,1]
[0,2]
[0,3]
[0,4]

[0,4]
  [1,3]
  [1,4]
  [2,5]
  [2,6]
  [3,4]
  [4,5]
  [4,7]
      [5,6]
      [5,7]
      [6,7]
      [6,8]
      
      [7,8]

T = 20
  
[0,4,7,8]

"""

from typing import List

from collections import defaultdict


class Solution:
  def videoStitching(self, clips: List[List[int]], T: int) -> int:
    clip_start_to_end = defaultdict(lambda: -1)
    for start, end in clips:
      clip_start_to_end[start] = max(clip_start_to_end[start], end)

    range_start = 0
    range_end = clip_start_to_end[range_start]
    if range_end == -1:
      return -1
    count = 1
    range_start += 1
    while range_end < T:
      max_end = -1
      for start in range(range_start, range_end + 1):
        max_end = max(max_end, clip_start_to_end[start])
      if max_end == -1:
        return -1
      if max_end <= range_end:
        return -1
      range_start = range_end
      range_end = max_end
      count += 1

    return count


def test():
  s = Solution()

  assert s.videoStitching(
    clips=[[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
           [4, 5], [5, 7], [6, 9]], T=9) == 3

  assert s.videoStitching(clips=[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T=10) == 3

  assert s.videoStitching(clips=[[0, 1], [1, 2]], T=5) == -1

  assert s.videoStitching(clips=[[0, 4], [2, 8]], T=5) == 2
