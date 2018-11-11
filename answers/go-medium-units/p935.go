package gmedium

import (
	"math"
)

/**
 *
 class Solution {
    private static final int MOD = 1000000007;
    private static final int[][] moves = {
        {4, 6},
        {6, 8},
        {7, 9},
        {4, 8},
        {3, 9, 0},
        {},
        {1, 7, 0},
        {2, 6},
        {1, 3},
        {2, 4},
    };

    public int knightDialer(int N) {
        long[] dp = new long[10];
        Arrays.fill(dp, 1);
        for (long i = 1; i < N; ++i) {
            long[] next = new long[10];
            for (int u = 0; u < 10; ++u) {
                for (int v : moves[u]) {
                    next[v] += dp[u];
                    next[v] %= MOD;
                }
            }
            dp = next;
        }
        long sum = 0;
        for (int i = 0; i < 10; ++i) {
            sum += dp[i];
            sum %= MOD;
        }
        return (int)sum;
    }
}
*/

var dialStepsMemo = make(map[int]int)

func makeMemoKey(digit, steps int) int {
	return digit*10000 + steps
}

func dial0(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(0, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial4(rSteps) + dial6(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial1(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(1, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial6(rSteps) + dial8(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial2(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(2, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial7(rSteps) + dial9(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial3(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(3, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial4(rSteps) + dial8(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial4(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(4, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial0(rSteps) + dial3(rSteps) + dial9(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial5(remainSteps int) int {
	return 0
}

func dial6(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(6, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial0(rSteps) + dial7(rSteps) + dial1(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial7(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(7, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial6(rSteps) + dial2(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial8(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(8, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial1(rSteps) + dial3(rSteps)
	dialStepsMemo[key] = result
	return result
}

func dial9(remainSteps int) int {
	if remainSteps == 0 {
		return 1
	}
	key := makeMemoKey(9, remainSteps)
	result := dialStepsMemo[key]
	if result > 0 {
		return result
	}
	rSteps := remainSteps - 1
	result = dial4(rSteps) + dial2(rSteps)
	dialStepsMemo[key] = result
	return result
}

func knightDialer(N int) int {
	if N == 1 {
		return 10
	}
	result := 0
	mod := int(math.Pow10(9)) + 7
	result = (result + dial0(N-1)) % mod
	result = (result + dial1(N-1)) % mod
	result = (result + dial2(N-1)) % mod
	result = (result + dial3(N-1)) % mod
	result = (result + dial4(N-1)) % mod
	result = (result + dial5(N-1)) % mod
	result = (result + dial6(N-1)) % mod
	result = (result + dial7(N-1)) % mod
	result = (result + dial8(N-1)) % mod
	result = (result + dial9(N-1)) % mod
	return result % mod
}

func knightDialer2(N int) int {
	// 当 N = 1 时，只能走 0 步，所以次数是 初始可能放置的号码 ，也就是 10种可能。
	if N == 1 {
		return 10
	}
	result := 0
	mod := int(math.Pow10(9)) + 7
	// 在对应表盘中上下一步可走的选择。
	nextJumps := make(map[int][]int)
	nextJumps[0] = []int{4, 6}
	nextJumps[1] = []int{6, 8}
	nextJumps[2] = []int{7, 9}
	nextJumps[3] = []int{4, 8}
	nextJumps[4] = []int{0, 3, 9}
	nextJumps[5] = []int{}
	nextJumps[6] = []int{0, 1, 7}
	nextJumps[7] = []int{2, 6}
	nextJumps[8] = []int{1, 3}
	nextJumps[9] = []int{2, 4}
	// 创建一个0-9 的拨号盘,用于记录每一个号码被拨的次数.
	dialPanel := make([]int, 10)
	// 当 N 大于1 时。 第一步，每一个号码被括号的次数是1
	for i := range dialPanel {
		dialPanel[i] = 1
	}
	// 再走一步时，有10种可能。这个取决于第一步走的位置。
	// 将10种可能的走法的和加起来
	for step := 1; step < N-1; step++ {
		nextState := make([]int, 10)
		for i := 0; i < 10; i++ {
			nextMoves := nextJumps[i]
			for _, move := range nextMoves {
				nextMoves[move] += dialPanel[i]
				nextMoves[move] %= mod
			}
		}
		dialPanel = nextState
	}
	// 将所有拨号加起来。
	for _, count := range dialPanel {
		result += count
		result %= mod
	}
	return result % mod
}
