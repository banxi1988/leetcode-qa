package main

import (
	"fmt"
	"math"
)

type Good struct {
	Price int
	/// 是否有特价优惠
	Special bool
}

type Discount struct {
	/// 满多少
	Base int
	/// 减多少
	Cut int
}

func main() {
	n := 0
	m := 0
	fmt.Scan(&n, &m)
	goods := []Good{}
	for i := 0; i < n; i++ {
		price := 0
		flag := 0
		fmt.Scan(&price, &flag)
		good := Good{price, flag == 1}
		goods = append(goods, good)
	}

	discounts := []Discount{}
	for i := 0; i < m; i++ {
		base := 0
		cut := 0
		fmt.Scan(&base, &cut)

		discount := Discount{base, cut}
		discounts = append(discounts, discount)
	}
	// 选择单独特价
	cost1 := 0.0
	totalBase := 0.0
	for i := 0; i < n; i++ {
		good := goods[i]
		price := float64(good.Price)
		totalBase += price
		if good.Special {
			cost1 += price * 0.8
		} else {
			cost1 += price
		}
	}

	// 选择整体特惠。
	cost2 := 0.0
	maxCut := 0
	// find discount
	for i := 0; i < m; i++ {
		discount := discounts[i]
		if totalBase >= float64(discount.Base) {
			if discount.Cut > maxCut {
				maxCut = discount.Cut
			}
		}
	}

	cost2 = totalBase - float64(maxCut)

	minCost := math.Min(cost1, cost2)
	fmt.Printf("%.2f\n", minCost)

}
