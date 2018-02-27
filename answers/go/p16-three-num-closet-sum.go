package main

import "fmt"
import "sort"
import "math"

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	fmt.Println(nums, target)
	numCount := len(nums)
	closestSum := math.MaxInt64
    minDiff := math.MaxInt64
	for i := 0; i < numCount - 2; i++{
		for j := i+1; j < numCount - 1; j++{
			for k := j + 1; k < numCount; k++{
                sum := nums[i] + nums[j] + nums[k]
                diff1 := (target - sum) 
                diff := diff1
                
				if diff < 0 {
					diff = -diff
                }
				if diff < minDiff{
					minDiff = diff
					closestSum = sum
					fmt.Println(nums[i],nums[j],nums[k], closestSum)
				}else{
					if nums[i] == 2 && nums[j] == 16 {
						fmt.Println(nums[i], nums[j],nums[k])
					}
					// if closestSum >= target{
	                //     break
					// }
                }
			}
            
            // if closestSum >= target && nums[j] > 0{
            //     break
            // }
        }

        // if closestSum >= target && nums[i] > 0{
        //         break
        // }

	}
	return closestSum
}

func main(){
	fmt.Println(threeSumClosest([]int{-1,2,1,-4}, 1))
	fmt.Println(threeSumClosest([]int{-1,0,1,-4}, 1))
	fmt.Println(threeSumClosest([]int{-1,3,1,-4}, 1))
	fmt.Println(threeSumClosest([]int{2,3,4,6,7,8}, 10)) // 9
	fmt.Println(threeSumClosest([]int{1,2,4,8,16,32,64,128}, 82)) // 82 

	fmt.Println(threeSumClosest([]int{-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33}, 0)) //  0

	fmt.Println(threeSumClosest([]int{56,57,-47,-14,23,31,20,39,-51,7,-4,43,-53,32,
		24,56,-28,90,-75,-6,21,-100,41,-84,95,95,44,84,70,-22,-86,-6,90,-87,65,-28,
		-29,-94,98,-28,-100,23,-25,6,-56,-54,-5,53,-88,-25,-31,-71,-13,-62,73,-35,
		-78,16,99,97,84,-27,-43,-50,18,-16,-61,7,-17,16,-92,28,43,-38,-33,-27,84,
		-72,-100,-91,-97,-99,59,-63,73,99,98,-100,-37,-80,3,18,93,-81,12,-75,-43,
		99,10,10,-6,13,0,76,-82,-5,27,-38,-81,77,-55,-100,90,-32,-25,-15,-16,68,
		-6,87,65,-38,82,78,-61,87,-72,46,50,-60,86,39,69,85,-49,28}, -289))
}