package main

import (
	"fmt"
)

func findUnusedKey(keymap map[int]bool) int {
	for key, v := range keymap {
		if !v {
			return key
		}
	}
	return -1
}

func canVisitAllRooms(rooms [][]int) bool {
	// if used value is true
	keyUsedMap := make(map[int]bool)
	// 开始只有房间0 的钥匙
	keyUsedMap[0] = false
	for key := 0; key != -1; key = findUnusedKey(keyUsedMap) {
		room := rooms[key]
		keyUsedMap[key] = true
		for _, rk := range room {
			_, ok := keyUsedMap[rk]
			if !ok {
				keyUsedMap[rk] = false
			}
		}
	}

	return len(keyUsedMap) == len(rooms)
}

func main() {
	arrA := [][]int{
		{1},
		{2},
		{3},
		{},
	}
	arrB := [][]int{
		{1, 3},
		{3, 0, 1},
		{2},
		{0},
	}
	fmt.Println("true -> ", canVisitAllRooms(arrA))

	fmt.Println("false -> ", canVisitAllRooms(arrB))
}
