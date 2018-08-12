package leetcode

func possibleBipartition(N int, dislikes [][]int) bool {
	room1Blacklist := make(map[int]bool)
	room2Blacklist := make(map[int]bool)
	cur := 0
	for cur < len(dislikes) {
		dislike := dislikes[cur]
		p1 := dislike[0]
		p2 := dislike[1]
		p1CanGoRoom1 := !room1Blacklist[p1]
		p1CanGoRoom2 := !room2Blacklist[p1]
		p2CanGoRoom1 := !room1Blacklist[p2]
		p2CanGoRoom2 := !room2Blacklist[p2]

		if !p1CanGoRoom1 && !p2CanGoRoom1 {
			return false
		}
		if !p1CanGoRoom2 && !p2CanGoRoom2 {
			return false
		}

		if cur > 0 && p1CanGoRoom1 && p1CanGoRoom2 && p2CanGoRoom1 && p2CanGoRoom2 {
			// free pair,先放在后面，后面再处理
			dislikes = append(dislikes, dislike)
		} else {
			if p1CanGoRoom1 && p2CanGoRoom2 {
				// p1 -> room1
				// p2 -> room2
				room1Blacklist[p2] = true
				room2Blacklist[p1] = true
			} else if p1CanGoRoom2 && p2CanGoRoom1 {
				// p2 -> room1
				// p1 -> room2
				room1Blacklist[p1] = true
				room2Blacklist[p2] = true
			}
		}
		cur++

	}
	return true
}
