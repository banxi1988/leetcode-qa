package main 
import "fmt"
import "sort"

func twoSumBasic(numbers []int, target int) []int {
    for firstIndex,firstValue := range numbers {
		remind := target - firstValue
		if remind < firstValue{
			continue
		}
		for secondIndex := firstIndex + 1; secondIndex < len(numbers); secondIndex++ {
			sum := (firstValue + numbers[secondIndex])
			if  sum == target {
				return []int{firstIndex + 1, secondIndex + 1}
			}else if sum > target{
				break
			}
		}
	}
	return []int{0,0}
}

// inner search with binary search
func twoSum(numbers []int, target int) []int {
    for firstIndex,firstValue := range numbers {
		remind := target - firstValue
		if remind < firstValue{
			continue
		}
		remainNums := len(numbers) - firstIndex - 1
		secondBaseIndex := firstIndex + 1
		secondIndex := sort.Search(remainNums,func(i int) bool { return numbers[ secondBaseIndex + i] >= remind})
		if secondIndex < remainNums && numbers[secondBaseIndex + secondIndex] == remind{
			return []int{ firstIndex+1, secondBaseIndex +  secondIndex + 1}
		}

	}
	return []int{0,0}
}

func main(){
	result1 := twoSum([]int{2,2,3,4},4)
	fmt.Println(result1)

	result2 := twoSum([]int{2,3,4},6)
	fmt.Println(result2)

	result3 := twoSum([]int{3,24,50,79,88,150,345}, 200)
	fmt.Println(result3)
}