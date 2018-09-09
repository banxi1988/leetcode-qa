package gmedium

type RLEIterator struct {
	nums   []int
	counts []int
	cur    int
}

func RLEInteratorConstructor(A []int) RLEIterator {
	nums := make([]int, 5001)
	counts := make([]int, 5001)
	cur := 0
	for i := 0; i < len(A)-1; i += 2 {
		count, num := A[i], A[i+1]
		if count < 1 {
			continue
		}
		nums[cur] = num
		counts[cur] = count
		cur++
	}
	return RLEIterator{nums, counts, 0}
}

func (this *RLEIterator) Next(n int) int {
	if this.cur >= len(this.nums) {
		return -1
	}
	num := this.nums[this.cur]
	count := this.counts[this.cur]
	remain := count - n
	if remain <= 0 {
		this.cur++
	}
	if remain < 0 {
		return this.Next(n - count)
	} else if remain == 0 {
		return num
	} else {
		this.counts[this.cur] = remain
		return num
	}
}
