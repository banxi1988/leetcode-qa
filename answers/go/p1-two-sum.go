package main 
import "fmt"

func twoSum(nums []int, target int) []int {
    for firstIndex,firstValue := range nums {
		for secondIndex := firstIndex + 1; secondIndex < len(nums); secondIndex++ {
			if (firstValue + nums[secondIndex]) == target {
				return []int{firstIndex, secondIndex}
			}
		}
	}
	return []int{0,0}
}

func main(){
	result1 := twoSum([]int{2,3,7,11},13)
	fmt.Println(result1)
}