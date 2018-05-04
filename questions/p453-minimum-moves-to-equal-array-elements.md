Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

分析假充有三个数，a,b,c 。他们分别的移到次数是 x,y,z
那么就存在这样的关系。
1) (a + x) = (b + y) = (c + z) (并且) x,y,z >= 0
 我们需要求得 (x,y,z) 这三个数中的最大值。
2） 从一次只能增加 `n-1` 个数的这个关系来看。
 令 M = max(x,y,z)  ,即为移到次数。
 那么  M * (n-1) 为增加的次数。
 那么 M * (n-1) = (a + x) + (b + y) + (c + z) - (a + b + c)
  即： M*(n-1) = x + y + z = (x) + (a + x - b) + (a + x -c)
   即 M*(n-1) = 3x + 2a - b - c

为了保证,x,y,z >=0, 可以设定 X 为最小移到次数，a 为其中最小值，因为最小值需要移到最多的次数。
所以。 x = M
即 M * (n-1) = 3M + 2a - b - c
右边将 n 代入，并以 otherSum 表示除最小值之外的和。

即 M * (n-1) = n * M + (n-1) * a - otherSum

即 M = otherSum - (n-1) *a
