package ghard

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

type FreqStack struct {
	/// 数字出现次数 map
	numCountMap map[int]int
	/// 数字
	freqNumsMap map[int][]int
	/// 最常出现的数字
	maxCount int
}

func Constructor() FreqStack {
	return FreqStack{numCountMap: make(map[int]int), freqNumsMap: make(map[int][]int)}
}

func (this *FreqStack) Push(x int) {
	count, _ := this.numCountMap[x]
	count++
	this.numCountMap[x] = count
	freqNums, _ := this.freqNumsMap[count]
	freqNums = append(freqNums, x)
	this.freqNumsMap[count] = freqNums
	this.maxCount = max(count, this.maxCount)
}

func (this *FreqStack) Pop() int {
	maxCount := this.maxCount
	maxFreqNums := this.freqNumsMap[maxCount]
	freqNumCount := len(maxFreqNums)
	x := maxFreqNums[freqNumCount-1]
	maxFreqNums = maxFreqNums[0 : freqNumCount-1]
	if len(maxFreqNums) > 0 {
		this.freqNumsMap[maxCount] = maxFreqNums
	} else {
		// 如此此频率下数字没有了，
		// 1) 删除此映射
		// 2) 查找下一个 maxCount
		delete(this.freqNumsMap, maxCount)
		nextMaxCount := maxCount - 1
		for len(this.freqNumsMap[nextMaxCount]) < 1 && nextMaxCount > 0 {
			nextMaxCount--
		}
		this.maxCount = nextMaxCount

	}
	count, _ := this.numCountMap[x]
	this.numCountMap[x] = count - 1
	return x
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 */
