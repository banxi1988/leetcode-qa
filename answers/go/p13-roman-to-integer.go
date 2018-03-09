package main

import "fmt"
// Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）

func romanToInt(s string) int {
	sum := 0
	prevNum := 0
	romanIntMap := map[byte]int{'I':1,'V':5,'X':10,'L':50,'C':100,'D': 500,'M': 1000}

    for _, ch := range []byte(s){
		num := romanIntMap[ch]
		//左减数字必须为一位
		if prevNum > 0 && prevNum < num{
			sum  -= (prevNum * 2)
		}
		sum += num
		prevNum = num
	}
	return sum
}

func main(){
	fmt.Println("I = 1",romanToInt("I"))
	fmt.Println("II = 2",romanToInt("II"))
	fmt.Println("III = 3",romanToInt("III"))
	fmt.Println("IV = 4",romanToInt("IV"))
	fmt.Println("V = 5",romanToInt("V"))
	fmt.Println("VI = 6",romanToInt("VI"))
	fmt.Println("VII = 7",romanToInt("VII"))
	fmt.Println("VIII = 8",romanToInt("VIII"))
	fmt.Println("IX = 9",romanToInt("IX"))
	fmt.Println("X = 10",romanToInt("X"))
	fmt.Println("XI = 11",romanToInt("XI"))
	fmt.Println("XIX = 19",romanToInt("XIX"))

	//左减的数字有限制，仅限于I、X、C。比如45不可以写成VL，只能是XLV
	fmt.Println("VL = 45",romanToInt("VL"))
	//但是，左减时不可跨越一个位值。比如，99不可以用IC（ {\displaystyle 100-1} 100-1）表示，而是用XCIX（ {\displaystyle [100-10]+[10-1]} [100-10]+[10-1]）表示。（等同于阿拉伯数字每位数字分别表示。）
	fmt.Println("XCIX = 99",romanToInt("XCIX"))
	fmt.Println("CXCIX = 199",romanToInt("CXCIX"))

	fmt.Println("MCDXXXVII = 1437",romanToInt("MCDXXXVII"))
	fmt.Println("MMMCCCXXXIII = 3333",romanToInt("MMMCCCXXXIII"))

}