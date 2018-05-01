Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

一开始设计了一种根据 `pattern` 生成一个成分分析的 map,
然后再循环递进判断新生成的 map ，然后两个 map 是否相当进行判断。

```go
func makePatternMap(bytes []byte) map[byte]int {
	phitMap := make(map[byte]int)
	for i := 0; i < len(bytes); i++ {
		char := bytes[i]
		count, _ := phitMap[char]
		phitMap[char] = count + 1
	}
	return phitMap
}

func isMapEqual(map1, map2 map[byte]int) bool {
	// fmt.Println("map1:", map1)
	// fmt.Println("map2:", map2)
	for char, count := range map1 {
		count2, ok := map2[char]
		if !ok || count != count2 {
			return false
		}
	}
	return true
}

func findAnagrams(s, p string) []int {
	indices := []int{}
	slen := len(s)
	plen := len(p)
	if slen < plen {
		return indices
	}

	patternMap := makePatternMap([]byte(p))
	sbytes := []byte(s)
	for i := 0; i < (slen - plen + 1); i++ {
		plenBytes := sbytes[i : i+plen]
		smap := makePatternMap(plenBytes)
		if isMapEqual(patternMap, smap) {
			indices = append(indices, i)
		}
	}
	return indices
}
```


## 性能问题，
上面的解法最大的问题就是性能问题，
在一个 s 由 20001 个 a 组成的字符串和 p 由 10000 个由 a 组成的字符串的测试用例中。
上面的测试耗时超出时间限制。

然后想到一种滑动窗口比较的方式：

```go
func findAnagrams(s, p string) []int {
	indices := []int{}
	slen := len(s)
	plen := len(p)
	if slen < plen {
		return indices
	}

	patternSum := 0
	for i := 0; i < plen; i++ {
		patternSum += int(p[i])
	}

	moveSum := 0
	for i := 0; i < plen; i++ {
		moveSum += int(s[i])
	}
	if moveSum == patternSum {
		indices = append(indices, 0)
	}
	for i := plen; i < slen; i++ {
		moveSum -= int(s[i-plen])
		moveSum += int(s[i])
		if moveSum == patternSum {
			indices = append(indices, i-plen+1)
		}
	}
	return indices
}
```

但是对于这种两个非异构但是其和刚好相等的则判断错误：

```
"af"
"be"
```

由于通过求和来提取异构特征是不靠谱的。 
但是也还算是有进步，比较这种滑动窗口确实是比较高效的。
所以现在有两个方向：
1）看有没有其他特征提取方式，可以使用这种滑动窗口的算法。
2）再尝试优化基于 Hash 映射的成分分析算法。

最后是将这两种方法给结合起来：

```go
func findAnagrams(s, p string) []int {
	indices := []int{}
	slen := len(s)
	plen := len(p)
	if slen < plen {
		return indices
	}

	patternMap := makePatternMap([]byte(p))
	sbytes := []byte(s)
	moveMap := makePatternMap(sbytes[0:plen])
	prevWindowMatch := false
	if isMapEqual(patternMap, moveMap) {
		prevWindowMatch = true
		indices = append(indices, 0)
	}
	for i := plen; i < slen; i++ {
		removeChar := s[i-plen]
		addChar := s[i]
		if addChar == removeChar && prevWindowMatch {
			indices = append(indices, i-plen+1)
			prevWindowMatch = true
			continue
		}
		moveMap[removeChar] = moveMap[removeChar] - 1
		moveMap[addChar] = moveMap[addChar] + 1
		if isMapEqual(patternMap, moveMap) {
			prevWindowMatch = true
			indices = append(indices, i-plen+1)
		} else {
			prevWindowMatch = false
		}
	}
	return indices
}
```