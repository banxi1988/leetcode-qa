package gmedium

func backtrack(results *[]string, cur string, openCount int, closeCount int, maxPairs int) {
	if len(cur) == maxPairs*2 {
		*results = append(*results, cur)
		return
	}
	if openCount < maxPairs {
		backtrack(results, cur+"(", openCount+1, closeCount, maxPairs)
	}
	if closeCount < openCount {
		backtrack(results, cur+")", openCount, closeCount+1, maxPairs)
	}

}

func generateParenthesis(n int) []string {
	if n == 1 {
		return []string{"()"}
	} else if n == 2 {
		return []string{"()()", "(())"}
	}

	results := []string{}
	backtrack(&results, "", 0, 0, n)
	return results
}
