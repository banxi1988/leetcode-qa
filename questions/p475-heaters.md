Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.


## 解题分析
对于任意的 houses 位置，及 heaters 位置。
假设需要的最小半径是 R
那么则要求.
`abs( min(heaters[m] - hourse[i], heaters[n] - hourse[i]) ) <= R,`
因为一个房屋即可以选择由左边的heater 的供肯暖，也可以由右边的 heater 来供暖。
所以我们需要的是
1. 根据 heater 位置 求出每一个房间需要供暖的最小半径。
2. 根据求出的所有房间供暖需要的最短半径，求其最大值。

这样得出第一个解法：

```go

func findRadius(houses []int, heaters []int) int {
	MaxInt := int(^uint(0) >> 1)
	heatersCount := len(heaters)
	calcMinRadius := func(hoursePosition int) int {
		minRadius := MaxInt
		for j := 0; j < heatersCount; j++ {
			radius := heaters[j] - hoursePosition
			if radius < 0 {
				radius = -radius
			}
			if radius < minRadius {
				minRadius = radius
			}
		}
		return minRadius
	}

	maxRadiu := 0
	for i := 0; i < len(houses); i++ {
		radius := calcMinRadius(houses[i])
		// fmt.Println("house position:", houses[i], " minHeaterRadius:", radius)
		if radius > maxRadiu {
			maxRadiu = radius
		}
	}
	return maxRadiu
}
```

但是在一些极端的测试用例中，有计算超时的问题。 所以需要优化上面的解法。


### 解法的优化

1. 排序 ，虽然示例数据都是有序的，但是有的测试用例的数据是无序的。

```go
	sort.Ints(houses)
	sort.Ints(heaters)
```

2. 查找最接近距离的供暖器位置的索引

```go
		// find the nearest heater position
		index := sort.SearchInts(heaters, hoursePosition)
```

3. 然后计算附近的供暖器的的半径

```go
	nearestIndex := min(heatersCount-1, index)
		nearestHeaterPosition := heaters[nearestIndex]
		radius := abs(hoursePosition - nearestHeaterPosition)
		if radius < minRadius {
			minRadius = radius
		}

		leftIndex := max(0, index-1)
		leftMinRadius := abs(hoursePosition - heaters[leftIndex])
		if leftMinRadius < minRadius {
			minRadius = leftMinRadius
		}
		rightIndex := min(index+1, heatersCount-1)
		rightMinRadius := abs(heaters[rightIndex] - hoursePosition)
		if rightMinRadius < minRadius {
			minRadius = rightMinRadius
		}
```




