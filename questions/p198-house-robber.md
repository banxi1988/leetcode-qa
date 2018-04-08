你是一个专业的强盗，计划抢劫沿街的房屋。每间房都藏有一定的现金，阻止你抢劫他们的唯一的制约因素就是相邻的房屋有保安系统连接，如果两间相邻的房屋在同一晚上被闯入，它会自动联系警方。

给定一个代表每个房屋的金额的非负整数列表，确定你可以在没有提醒警方的情况下抢劫的最高金额。


解法说明：先使用递归将基本的算法写出

```go
func rob(nums []int) int {
	numCount := len(nums)
	if numCount < 1 {
		return 0
	}
	if numCount == 1 {
		return nums[0]
	}
	if numCount == 2 {
		return max(nums[0], nums[1])
	}
	// take first
	first := nums[0]
	max1 := first + rob(nums[2:])
	// ignore first one
	max2 := rob(nums[1:])
	return max(max1, max2)
}
```

然后再改成非递归的。

```go

// RobOption is a type
type RobOption struct {
	Robbed           int
	AvailableHourses []int
}

func rob(nums []int) int {
	optionList := []RobOption{RobOption{AvailableHourses: nums}}
	income := 0

	for len(optionList) > 0 {
		option := optionList[0]
		optionList = optionList[1:]
		optionNums := option.AvailableHourses
		numsCount := len(optionNums)
		switch numsCount {
		case 0:
			break
		case 1:
			income = max(optionNums[0]+option.Robbed, income)
		case 2:
			income = max(income, max(optionNums[0]+option.Robbed, optionNums[1]+option.Robbed))
		default:
			// option 1 rob the first house
			option1 := RobOption{Robbed: option.Robbed + optionNums[0], AvailableHourses: optionNums[2:]}
			optionList = append(optionList, option1)
			// option 2 ignore the first house
			option2 := RobOption{Robbed: option.Robbed, AvailableHourses: optionNums[1:]}
			optionList = append(optionList, option2)
		}
		// fmt.Println("optionList count :", len(optionList))

	}
	return income

}

```

不过即使改成了非递归的，整个时间还是超出限制，甚至需要更多的时间。

再次回到递归上面，其实只需要记录第一个抢的最大可能值 和不抢的最大可能值，两个数的比较。
因为如果连续两个不抢比如 1,1,2,3。从 `2` 开始抢肯定不如从`1`开始抢的收益大，因为至少会多一份收益。
原来的循环和递归没有利用这一点，导致时间复杂度非常高。

增加一个 Pass 字段，来记录上一家有没有抢，如果连续两次忽略选项列表排除，这样增加了一些速度。
```go
default:
			// option 1 rob the first house
			option1 := RobOption{Robbed: option.Robbed + optionNums[0], AvailableHourses: optionNums[2:], Pass: false}
			optionList = append(optionList, option1)
			if !option.Pass {
				// 如果连续不抢，肯定不会有更大的收益
				// option 2 ignore the first house
				option2 := RobOption{Robbed: option.Robbed, AvailableHourses: optionNums[1:], Pass: true}
				optionList = append(optionList, option2)
			}
		}
```

然后将该问题进一步抽象。假充我们在第 i 间要抢房子的前面。我们的收益只有两种可能，就是抢不抢第 i 间房子。
设置 robbed[i] 为抢第i 间房子的最大收益 ，pass[i] 为不抢第 i 间房子的最大收益 。
那此时最大的收益便是 

```
max(robbed[i], pass[i])
robbed[i] = nums[i] + pass[i-1] // 要抢第 i 间的前提是 第 i-1 间不抢
pass[i] = max(rob[i-1], pass[i-1]) // 第 i 间不抢的最大值是 第 i-1抢的最大收益 与第 i-1 间不抢的最大收益的最大值。
```
因此只需要两个数来记录前 i-1 项的两个不同的最大收益 即可。

参考自： http://mzorro.me/2016/03/15/leetcode-house-robber/