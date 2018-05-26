package main

import "fmt"

func consecutiveNumbersSum(N int) int {
	// e^2 - 2N + e = s^2 - s
	compCount := 1 // one for self
	doubleN := N * 2
	// maxK := int(math.Sqrt(float64(N+1))) + 1
	for k := 2; k <= N; k++ {
		if doubleN%k != 0 {
			continue
		}
		// 即 `e + s = 2N/k` 及 `e - s = k - 1`
		// 其中要求 2N 是 k 的倍数
		// let m = e + s
		// let n = e - s
		// ie e = n + s
		// ie m = n + s + s
		// s = (m -n)/2

		m := doubleN / k
		n := k - 1
		mSubn := m - n
		if mSubn%2 != 0 {
			continue
		}
		s := mSubn / 2
		e := n + s
		fmt.Println(s, e)
		if s > 0 && e > 0 {
			compCount++
		}
	}
	return compCount
}

func main() {
	// fmt.Println(" 2 -> ", consecutiveNumbersSum(5))
	// fmt.Println(" 2 -> ", consecutiveNumbersSum(3))
	// fmt.Println(" 3 -> ", consecutiveNumbersSum(9))
	// fmt.Println(" 4 -> ", consecutiveNumbersSum(15))
	fmt.Println(" 6 -> ", consecutiveNumbersSum(45))
	// fmt.Println(" 4 -> ", consecutiveNumbersSum(77601076))
	// fmt.Println(" 16 -> ", consecutiveNumbersSum(68188380))
	// start := time.Now()
	// for i := 0; i < 10; i++ {
	// 	consecutiveNumbersSum(77601076)
	// 	consecutiveNumbersSum(68188380)
	// }
	// fmt.Println("duration: ", time.Since(start))
}
