package gmedium

type StockSpanner struct {
	prices     []int
	priceCount int
}

func StockSpannerConstructor() StockSpanner {
	return StockSpanner{prices: make([]int, 10010), priceCount: 0}
}

func (this *StockSpanner) Next(price int) int {
	this.prices[this.priceCount] = price
	span := 0
	for i := this.priceCount; i > -1; i-- {
		if this.prices[i] <= price {
			span++
		} else {
			break
		}
	}
	this.priceCount++
	return span
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
