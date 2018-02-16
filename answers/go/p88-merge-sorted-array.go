package main 
import "fmt"

// 主要的特点是有序数组。
// 可以使用一个临时数据用来保存合并的结果 。


func merge(nums1 []int, m int, nums2 []int, n int)  {
   nums1_index := 0
   nums2_index := 0
   nums := []int{}

   for nums1_index < m && nums2_index < n{
		num1 := nums1[nums1_index]
		num2 := nums2[nums2_index]
		if num1 < num2{
			nums = append(nums,num1)
			nums1_index++
		}else{
			nums = append(nums,num2)
			nums2_index++
		}
	} 

	if nums1_index < m{
		nums = append(nums,nums1[nums1_index:m]...)
	}else{
		nums = append(nums,nums2[nums2_index:n]...)
	}
	copy(nums1,nums)
}

func main(){
	nums1 := []int{6,8,16,0,0}
	nums2 := []int{17,18}
	merge(nums1,3,nums2,2)
	fmt.Println(nums1)
}