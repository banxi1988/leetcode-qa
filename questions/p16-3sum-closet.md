
给定一个包括 n 个整数的数组 S，找出 S 中的三个整数使得他们的和与给定的数 target 最接近。返回这三个数的和。假定每组输入只存在一个答案。

例如，给定数组 S = {-1 2 1 -4}, 并且 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


首先先将暴力解法写出来：

暴力解法主要就是通过三层循环遍历所有可能的组合来判断其各与目标值最小的组合。

```go
func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	fmt.Println(nums)
	numCount := len(nums)
	closestSum := math.MaxInt64
	minDiff := math.MaxInt64
	for i := 0; i < numCount - 2; i++{
		for j := i+1; j < numCount - 1; j++{
            sum1 := nums[i] + nums[j]
			for k := j + 1; k < numCount; k++{
                sum := sum1 + nums[k]
                diff1 := (target - sum) 
                diff := diff1
                
				if diff < 0 {
					diff = -diff
                }
				if diff < minDiff{
					minDiff = diff
					closestSum = sum
				}
			}
        }

	}
	return closestSum
}
```

优化方法：
一个直接的优化目标就是减少循环次数。
首先先排序。
由于已经排序了按照上面的循环遍历规则就是越往后面的组合，他们的和就越大。

如果目标值是在和中间的话，那

对于第三层循环来说，当和大于 target 时。后面他们的距离（即相差值）将越来越大。

所以对于第三层循环有一个中止条件就是。 `diff >= minDiff`

对于第二层循环来说。 找出第二层循环的中止条件就稍微复杂一些了。

i,  j  k
2,3,4,,6,7,8,9 -> 2,3,5 (target:10)



当第三层循环结束之后。 说明在当前的第二层循环的条件下，已经找到三数和的相近值。

```go
func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	fmt.Println(nums)
	numCount := len(nums)
	closestSum := math.MaxInt64
    minDiff := math.MaxInt64
    numi := 0
    numj := 0
    numk := 0
   
	for i := 0; i < numCount - 2; i++{
        numi = nums[i]
		for j := i+1; j < numCount - 1; j++{
            numj = nums[j]
            sum1 := numsi + numsj
			for k := j + 1; k < numCount; k++{
                numk = nums[k]
                sum := sum1 
                diff1 := (target - sum) 
                diff := diff1
                
				if diff < 0 {
					diff = -diff
                }
				if diff < minDiff{
					minDiff = diff
					closestSum = sum
				}else{
                    break
                }
            }
            
            if closestSum >= target{
                break
            }
        }

        if closestSum >= target{
                break
        }

	}
	return closestSum
}
```

上面的优化方式在实际提交测试之后发现有问题。

