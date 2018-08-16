package leetcode

// const MAX_BUCKET = 100

type Entry struct {
	Key   int
	Value int
}

type MyHashMap struct {
	hashArray [MAX_BUCKET][]Entry
}

/** Initialize your data structure here. */
func ConstructorHashMap() MyHashMap {
	return MyHashMap{hashArray: [MAX_BUCKET][]Entry{}}
}

/** value will always be positive. */
func (this *MyHashMap) Put(key int, value int) {
	index := key % MAX_BUCKET
	entries := this.hashArray[index]
	for index, entry := range entries {
		if entry.Key == key {
			entry.Value = value
			entries[index] = entry
			return
		}
	}

	entries = append(entries, Entry{key, value})
	this.hashArray[index] = entries
}

/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
	index := key % MAX_BUCKET
	entries := this.hashArray[index]
	for _, entry := range entries {
		if entry.Key == key {
			return entry.Value
		}
	}
	return -1
}

/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int) {
	index := key % MAX_BUCKET
	entries := this.hashArray[index]
	indexToDelete := -1
	for index, entry := range entries {
		if entry.Key == key {
			indexToDelete = index
			break
		}
	}
	if indexToDelete != -1 {
		if indexToDelete == 0 {
			entries = entries[1:]
		} else if indexToDelete+1 == len(entries) {
			entries = entries[:len(entries)-1]
		} else {
			entries = append(entries[:indexToDelete], entries[indexToDelete+1:]...)
		}
		this.hashArray[index] = entries
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
