
给定一个包含 n 个整数的数组 S，是否存在属于 S 的三个元素 a，b，c 使得 a + b + c = 0 ？找出所有不重复的三个元素组合使三个数的和为零。

注意：结果不能包括重复的三个数的组合。

例如, 给定数组 S = [-1, 0, 1, 2, -1, -4]，

一个结果集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


## 解答分析
1. 集合的不同可以以组合排序后的字符串表示作为唯一性判断。
2. 最简单的解法还是遍历.

这样得到的初步解答如下：

```go
import "sort"
import "bytes"
import "strconv"

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	numsmap := make(map[string]bool)
	numsets := make([][]int, 0, len(numsmap))
	numCount := len(nums)

	for i := 0; i < numCount - 2; i++{
		numi := nums[i]
		if numi > 0{
			break
		}
		for j := i+1; j < numCount - 1; j++{
			numj := nums[j]
			sumij := numi + numj
			if sumij > 0{
				break
			}
			for k := j + 1; k < numCount; k++{
				numk := nums[k]
				sum := sumij + numk
				if sum > 0 {
					break
				}else if sum == 0{
					var buf  bytes.Buffer
					buf.WriteString(strconv.Itoa(numi))
					buf.WriteString(strconv.Itoa(numj))
					buf.WriteString(strconv.Itoa(numk))
					key := buf.String()
					_, exists := numsmap[key]
					if !exists{
						numsmap[key] = true
						numsets = append(numsets,[]int{numi,numj,numk})
					}

					break
				}
				
			}

        }
	}
	return numsets
}

```

上面的解答在提交之后。

>311 / 313 个通过测试用例 Time Limit Exceeded

也就是思考是对的，但是耗时太高。

在判断最后一个数是使用了二分查找。加快了速度。

```go

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	numsmap := make(map[string]bool)
	numsets := [][]int{}
	numCount := len(nums)

	if numCount < 3 || nums[numCount -1] < 0{
		return numsets
	}
	for i := 0; i < numCount - 2; i++{
		numi := nums[i]
		if numi > 0{
			break
		}
		for j := i+1; j < numCount - 1; j++{
			numj := nums[j]
			sumij := numi + numj
			if sumij > 0{
				break
			}
			targetNumk := 0 - sumij
			remainNums := nums[j+1:]
			kindex := sort.SearchInts(remainNums,targetNumk)
			if kindex < len(remainNums)  {
				if remainNums[kindex] == targetNumk{
					var buf  bytes.Buffer
					buf.WriteString(strconv.Itoa(numi))
					buf.WriteString(strconv.Itoa(numj))
					buf.WriteString(strconv.Itoa(targetNumk))
					key := buf.String()
					_, exists := numsmap[key]
					if !exists{
						numsmap[key] = true
						numsets = append(numsets,[]int{numi,numj,targetNumk})
					}
				}else if kindex == 0 {
					break // 需要一个更小的数，但是不可能了。后面数会越来越大
				}
			}
		

        }
	}
	return numsets
}
```

但是在处理最后一组全0的输入时还是超时了

> 313 / 313 个通过测试用例 状态：Time Limit Exceeded