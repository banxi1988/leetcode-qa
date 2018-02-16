Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

```c
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

因为限定了是两个数想加，所以可以尝试暴力解法：
也就是
先选择第一个数，信次遍历后面的数与之想加，如果想加之和等于 target 即找到了对应的解了。

```c
int* twoSum(int* nums, int numsSize, int target) {
    int *result = malloc(sizeof(int) * 2);
    int first = 0;
    int second = 1;
    for(first = 0;first < numsSize;first++){
        for(second = first + 1; second < numsSize;second++){
                if((nums[first] + nums[second]) == target){
                    result[0] = first;
                    result[1] = second;
                    return result;
                }
        }
    }
    return NULL;
}
```

上面解释的算法复杂度为 `(n-1) + (n-2) + ... + 1  ~= n^2`

可能优化方法：

由于是求和，有一种可能的优化方向是先对数组进行排序。
这样的话可以有种情况可以减少循环。
1）如果 `first` 就已经大于 `target` ,那么肯定不再存在对应的解，另外就是后面的数也不需要再遍历，因为是已经排好序的了。
2）同上可以对 `second` 也做如上的判断也减少第二层循环。

排序的算法最好的情况可以达到  `log2N`
但是对于单次的查找而言，对于最坏的情况，就增加了排序了这个复杂度了。


## Two Sum II

two sum II 这个问题则是有一个前提是已经排序好了的值。
那除了遍历之外可以增加两个提前终止循环的条件：

1) 提前终止第一层循环的条件。

```go
		remind := target - firstValue
		if remind < firstValue{
			continue
		}
```

2） 终止第二层循环的条件

```go
            if  sum == target {
				return []int{firstIndex + 1, secondIndex + 1}
			}else if sum > target{
				break
			}
```

如何进一步优化？

1） 第二层循环由于相当是去寻找一个相当的值了。所以可以使用二分查找来优化。

优化后的内层循环如下：

```go
		remainNums := len(numbers) - firstIndex - 1
		secondBaseIndex := firstIndex + 1
		secondIndex := sort.Search(remainNums,func(i int) bool { return numbers[ secondBaseIndex + i] >= remind})
		if secondIndex < remainNums && numbers[secondBaseIndex + secondIndex] == remind{
			return []int{ firstIndex+1, secondBaseIndex +  secondIndex + 1}
		}
```


## Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

```c
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True

```


Example 2:

```c
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
```



