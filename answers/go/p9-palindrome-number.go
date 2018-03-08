package main

import "fmt"
import "math"

func isPalindrome(x int) bool {
   if x < 0{
	   return false
   } 
   if x < 10{
	   return true
   }
   // 数字个数 10 -> 2
   digitCount := int(math.Log10(float64(x))) + 1
   start := 1
   end := digitCount
   xEnd := x
   xStart := x

   endBase := int(math.Pow10(end - 1))
   for start < end{
		endDigit := xEnd / endBase
		startDigit := xStart % 10
		if endDigit != startDigit{
			return false
		}
		xEnd = xEnd % endBase
		endBase /= 10
		xStart /= 10
		start++
		end--
		
   } 
   return true
}

func main(){
	fmt.Println("isPalindrome(-1)", isPalindrome(-1))
	fmt.Println("isPalindrome(1)", isPalindrome(1))
	fmt.Println("isPalindrome(11)", isPalindrome(11))
	fmt.Println("isPalindrome(121)", isPalindrome(121))
	fmt.Println("isPalindrome(1221)", isPalindrome(1221))
	fmt.Println("isPalindrome(2147483648)", isPalindrome(2147483648))
}