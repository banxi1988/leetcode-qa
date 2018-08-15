package leetcode

import (
	"sort"
)

type MyHashSet struct {
	hashArray [100][]int
}

const MAX_BUCKET = 100

/** Initialize your data structure here. */
func Constructor() MyHashSet {
	set := MyHashSet{hashArray: [100][]int{}}
	return set
}

func (this *MyHashSet) Add(key int) {
	index := key % MAX_BUCKET
	nums := this.hashArray[index]
	numCount := len(nums)
	if numCount == 0 {
		nums = append(nums, key)
	} else {
		i := sort.SearchInts(nums, key)
		if i < numCount && nums[i] == key {
			// already exits
			return
		}
		if i == numCount {
			nums = append(nums, key)
		} else {
			nums = append(nums[:i], append([]int{key}, nums[i:]...)...)
		}
	}
	this.hashArray[index] = nums

}

func (this *MyHashSet) Remove(key int) {
	index := key % MAX_BUCKET
	nums := this.hashArray[index]
	i := sort.SearchInts(nums, key)
	if i < len(nums) && nums[i] == key {
		nums = append(nums[:i], nums[i+1:]...)
		this.hashArray[index] = nums
	}
}

/** Returns true if this set did not already contain the specified element */
func (this *MyHashSet) Contains(key int) bool {
	index := key % MAX_BUCKET
	nums := this.hashArray[index]
	i := sort.SearchInts(nums, key)
	return i < len(nums) && nums[i] == key
}
