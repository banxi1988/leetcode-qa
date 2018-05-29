package main

import (
	"fmt"
)

type Cola struct {
	Kind  int
	Mei   int
	Tuan  int
	Happy float64
}

func main() {
	N := 0
	M := 0
	Kinds := 0
	fmt.Scan(&N, &M, &Kinds)

	colas := make([]Cola, Kinds)
	maxHappy := 0.0
	meiWeight := float64(M) / float64(N)
	tuanWeight := 1 - meiWeight
	meiMaxHappy := 0
	tuanMaxHappy := 0
	for i := 0; i < Kinds; i++ {
		a := 0
		b := 0
		fmt.Scan(&a, &b)
		happy := float64(a)*meiWeight + float64(b)*tuanWeight
		cola := Cola{i, a, b, happy}
		colas[i] = cola
		if happy > maxHappy {
			maxHappy = happy
		}
		if a > meiMaxHappy {
			meiMaxHappy = a
		}
		if b > tuanMaxHappy {
			tuanMaxHappy = b
		}
	}
	bestColas := []Cola{}
	// meiBestColas := []Cola{}
	// tuanBestColas := []Cola{}
	for i := 0; i < len(colas); i++ {
		cola := colas[i]
		if cola.Happy == maxHappy {
			bestColas = append(bestColas, cola)
		}
		// if cola.Mei == meiMaxHappy {
		// 	meiBestColas = append(meiBestColas, cola)
		// }
		// if cola.Tuan == tuanMaxHappy {
		// 	tuanBestColas = append(tuanBestColas, cola)
		// }
	}
	bestKind := bestColas[len(bestColas)-1].Kind
	// meiBestKind := meiBestColas[len(meiBestColas)-1].Kind
	// tuanBestKind := tuanBestColas[len(tuanBestColas)-1].Kind
	for i := 0; i < Kinds; i++ {
		if i > 0 {
			fmt.Print(" ")
		}
		if i == bestKind {
			fmt.Print(N)
		} else {
			fmt.Print("0")
		}
	}
	fmt.Print("\n")

}
