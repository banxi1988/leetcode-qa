Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

首先是一个根据结构特征的解答。但是下面的解答有问题就是没有考虑到。 另一个限制:
> No two characters may map to the same character but a character may map to itself.


```go
func isIsomorphic(s string, t string) bool {
	charCount := len(s)
	if charCount < 2 {
		return true
	}
	prevSchar := s[0]
	prevTchar := t[0]
	sflags := 1
	tflags := 1
	for i := 1; i < charCount; i++ {
		sch := s[i]
		tch := t[i]

		if sch == prevSchar {
			sflags++
		}
		if tch == prevTchar {
			tflags++
		}

		if sflags != tflags {
			return false
		}

		prevSchar = sch
		prevTchar = tch
	}
	return true
}
```

修改之后，使用一个 map 来记录已经映射过的结果。 如果再次有映射发现不同的话则返回错误：

```go

func isIsomorphic(s string, t string) bool {
	charCount := len(s)
	if charCount < 2 {
		return true
	}
	prevSchar := s[0]
	prevTchar := t[0]
	sflags := 1
	tflags := 1

	s2tMap := make(map[byte]byte)
	s2tMap[prevSchar] = prevTchar

	for i := 1; i < charCount; i++ {
		sch := s[i]
		tch := t[i]

		if sch == prevSchar {
			sflags++
		}
		if tch == prevTchar {
			tflags++
		}

		if sflags != tflags {
			return false
		}

		mapedTch, ok := s2tMap[sch]
		if ok {
			if mapedTch != tch {
				return false
			}
		} else {
			s2tMap[sch] = tch
		}

		prevSchar = sch
		prevTchar = tch
	}
	return true
}
```