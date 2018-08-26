package ghard

type FreqStack struct {
	/// 数字出现次数 map
	numCountMap map[int]int
	/// 数字栈
	numStack []int
}

func Constructor() FreqStack {
	return FreqStack{numCountMap: make(map[int]int), numStack: []int{}}
}

func (this *FreqStack) Push(x int) {
	this.numStack = append(this.numStack, x)
	count, _ := this.numCountMap[x]
	this.numCountMap[x] = count + 1
}

func contains(slice []int, x int) bool {
	for _, num := range slice {
		if num == x {
			return true
		}
	}
	return false
}

func (this *FreqStack) Pop() int {
	maxCount := 0
	for _, count := range this.numCountMap {
		if count > maxCount {
			maxCount = count
		}
	}
	maxCountNums := []int{}
	for num, count := range this.numCountMap {
		if count == maxCount {
			maxCountNums = append(maxCountNums, num)
		}
	}
	for i := len(this.numStack) - 1; i > -1; i-- {
		num := this.numStack[i]
		if contains(maxCountNums, num) {
			this.numStack = append(this.numStack[:i], this.numStack[i+1:]...)
			count, _ := this.numCountMap[num]
			this.numCountMap[num] = count - 1
			return num
		}
	}
	return -1
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 */
