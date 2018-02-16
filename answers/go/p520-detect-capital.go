package main
import "fmt"

import "unicode"

func detectCapitalUse(word string) bool {
	upper := true
	lower := true
	normal := true
	
   for index,char := range word{
	 upper = upper && unicode.IsUpper(char)
	 lower = lower && unicode.IsLower(char)
	 if index == 0{
		 normal = unicode.IsUpper(char)
	 }else{
		 normal = normal && unicode.IsLower(char) 
	 }
	if !(upper || lower || normal){
		return false
	}

   } 
   return upper || lower || normal
}

func main(){
	fmt.Println("USA ",detectCapitalUse("USA"))
	fmt.Println("USa ",detectCapitalUse("USa"))
	fmt.Println("Flag ",detectCapitalUse("Flag"))
	fmt.Println("FlaG ",detectCapitalUse("FlaG"))
	fmt.Println("flaG ",detectCapitalUse("flaG"))
	fmt.Println("F ",detectCapitalUse("F"))
	fmt.Println("leetcode ",detectCapitalUse("leetcode"))

}