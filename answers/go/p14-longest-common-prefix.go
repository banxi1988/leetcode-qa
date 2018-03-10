package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0{
		return ""
	}
	commonLen := len(strs[0])
	for _,str := range strs{
		len1 := len(str)
		if len1 < commonLen{
			commonLen = len1
		}
	}
	maxLen := 0
	for maxLen < commonLen {
		chIndex := maxLen
		ch := strs[0][chIndex]
		allEqual := true
		for _,str := range strs{
			if str[chIndex] != ch{
				allEqual = false
				break
			}
		}
		if allEqual{
			maxLen += 1
		}else{
			break
		}
	}
	return strs[0][:maxLen]
}


func main(){
	fmt.Println(longestCommonPrefix([]string{"aca","cba"}))
	fmt.Println(longestCommonPrefix([]string{"abc","abcd"}))
	fmt.Println(longestCommonPrefix([]string{"abc","edf"}))
	fmt.Println(longestCommonPrefix([]string{"","edf"}))
}