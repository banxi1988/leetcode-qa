package geasy

// RecentCounter 统计
type RecentCounter struct {
	records []int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

func (this *RecentCounter) Ping(t int) int {
	records := this.records
	minT := t - 3000
	startIndex := len(records)
	for i, value := range records {
		if value >= minT {
			startIndex = i
			break
		}
	}
	records = records[startIndex:]
	records = append(records, t)
	this.records = records
	// fmt.Println("records:", records)
	return len(records)
}
