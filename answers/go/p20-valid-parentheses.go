package main

import "fmt"

func isValid(s string) bool{
	stack := []byte{}
	parentheseMap := map[byte]byte{'(':')','[':']','{':'}'}
	for _,ch := range []byte(s){
		if len(stack) == 0{
			stack = append(stack,ch)
		}else{
			topCh := stack[len(stack) -1]
			pairCh := parentheseMap[topCh]
			if pairCh == ch{
				stack = stack[:len(stack) - 1]
			}else{
				stack = append(stack,ch)
			}
		}
	}
	return len(stack) == 0
}

func main(){
	fmt.Println("( false ", isValid("("))
	fmt.Println(") false", isValid(")"))
	fmt.Println("[) false", isValid("[)"))
	fmt.Println("()", isValid("()"))
	fmt.Println("[]", isValid("[]"))
	fmt.Println("{}", isValid("{}"))
	fmt.Println("{}[]", isValid("{}[]"))
	fmt.Println("{[]}", isValid("{[]}"))
	fmt.Println("{[}] false ", isValid("{[}]"))
}