You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

首先是一个递归的解法：

```go
func canWinNim(n int) bool {
	switch n {
	case 1:
		return true
	case 2:
		return true
	case 3:
		return true
	case 4:
		return false
	default:
		canWin1 := !canWinNim(n - 1)
		canWin2 := !canWinNim(n - 2)
		canWin3 := !canWinNim(n - 3)
		return canWin1 || canWin2 || canWin3
	}
}

```

但是超时了，于是加了一点缓存。

```go
var canWinMap = make(map[int]bool)

func canWinNim(n int) bool {
	win, ok := canWinMap[n]
	if ok {
		return win
	}
	switch n {
	case 1:
		return true
	case 2:
		return true
	case 3:
		return true
	case 4:
		return false
	default:
		canWin1 := !canWinNim(n - 1)
		canWin2 := !canWinNim(n - 2)
		canWin3 := !canWinNim(n - 3)
		win := canWin1 || canWin2 || canWin3
		canWinMap[n] = win
		return win
	}
}
```

但是还是超时了，所以必须得将尾递归改成迭代才行。

有一个优化就是取余：

```go
func canWinNim(n int) bool {
	return n%4 != 0
}
```
因为 4 是必败的数，然后，5，6，7 是必胜数。然后到 8 又是必败数。
所以只要是 4 的倍数，先手就是必败。

