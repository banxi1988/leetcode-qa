package gmedium

import (
	"sort"
	"strconv"
	"strings"
)

func joinNums(arr []int, sep string) string {
	numCount := len(arr)
	if numCount == 0 {
		return ""
	}
	strs := make([]string, numCount)
	for i := 0; i < numCount; i++ {
		strs[i] = strconv.Itoa(arr[i])
	}
	return strings.Join(strs, sep)
}

func fourSum(nums []int, target int) [][]int {
	resultMap := make(map[string][]int)
	sort.Ints(nums)
	numCount := len(nums)
	for i := 0; i < numCount-3; i++ {
		numi := nums[i]
		if numi > target && numi >= 0 {
			break
		}
		for j := i + 1; j < numCount-2; j++ {
			numj := nums[j]
			sumij := numi + numj
			if sumij > target && numj >= 0 {
				break
			}
			for k := j + 1; k < numCount-1; k++ {
				numk := nums[k]
				sumijk := sumij + numk
				if sumijk > target && numk >= 0 {
					break
				}
				for g := k + 1; g < numCount; g++ {
					numg := nums[g]
					sumijkg := sumijk + numg
					if sumijkg == target {
						tuple := []int{numi, numj, numk, numg}
						key := joinNums(tuple, "")
						resultMap[key] = tuple
					} else if sumijkg > target && numg >= 0 {
						break
					}
				}
			}
		}
	}
	result := [][]int{}
	for _, tuple := range resultMap {
		result = append(result, tuple)
	}
	return result
}
