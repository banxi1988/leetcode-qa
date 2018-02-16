package main 
import "fmt"

func convertToTitle(n int) string {
	var chars []rune
   // 1 -> A
   // 2-> B
   // 27 -> AA
   // 28 -> AB
   // 702 -> ZZ
   // 703 -> AAA
   num := n
   for num > 26{
	   reminder := num % 26
	   if reminder == 0{
		   reminder = 26
		   num -= 26
	   }
	   num /= 26
	   char := rune(reminder - 1 + 'A') 
	   chars = append(chars[:0], append([]rune{char},chars[0:]...)...)
   }
   char := rune(num - 1 + 'A')
   chars = append(chars[:0], append([]rune{char},chars[0:]...)...)
   return string(chars)
}

func main(){
	b := convertToTitle(1)
	fmt.Println("1 =",b)

	b = convertToTitle(10)
	fmt.Println("10 =",b)

	b = convertToTitle(26)
	fmt.Println("26 =",b)

	b = convertToTitle(27)
	fmt.Println("27 =",b)

	b = convertToTitle(28)
	fmt.Println("28 =",b)

	b = convertToTitle(700)
	fmt.Println("700 =",b)

	b = convertToTitle(701)
	fmt.Println("701 =",b)

	b = convertToTitle(702)
	fmt.Println("702 =",b)

	b = convertToTitle(703)
	fmt.Println("703 =",b)

	b = convertToTitle(768)
	fmt.Println("768 =",b)
}