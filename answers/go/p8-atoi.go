package main

import "fmt"

func myAtoi(str string) int {
	start := false
	num := 0
	intMax := 2147483647
	intMin := 2147483648
	var signChar byte = 0
	for _, ch := range []byte(str){
		// IsSpace
		if ch == '\t' || ch == '\n' || ch == '\v' || ch == '\f' || ch == '\r' || ch == ' ' || ch == 0x85 || ch == 0xa0{
			if start{
				break
			}else{
				continue
			}
		}else{
			start = true
			if ch == '+' || ch == '-'{
				if signChar == 0{
					signChar = ch
				}else{
					break
				}
			}else {
				if ch >= '0' && ch <= '9'{
					num = num * 10 + int(ch - '0')
					if num >= intMax && (signChar == 0 || signChar == '+'){
						return intMax
					}else if num >= intMin && signChar == '-'{
						return -intMin
					}
				}else{
					break
				}
			}
		}
   }
   if signChar == '-'{
		return -num
	}else{
		return num
	}
}

func main(){
	fmt.Println(`atoi(  123 4)=`,myAtoi(" 123 4"))
	fmt.Println(`atoi( a123)=`,myAtoi(" a123"))
	fmt.Println(`atoi(-1)=`,myAtoi("-1"))
	fmt.Println(`atoi(-123)=`,myAtoi("-123"))
	fmt.Println(`atoi(123abc)=`,myAtoi(" 123abc"))
	fmt.Println(`atoi(2147483649)=`,myAtoi("2147483649"))
}