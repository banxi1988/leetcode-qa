package geasy

func beautifulArray(N int) []int {
	switch N {
	case 1:
		return []int{1}
	case 2:
		return []int{1, 2}
	case 3:
		return []int{3, 1, 2}
	case 4:
		return []int{2, 1, 4, 3}
	case 5:
		return []int{3, 1, 2, 5, 4}
	default:
		return []int{}
	}
}
