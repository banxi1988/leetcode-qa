package main

import "fmt"

type MyStack struct {
	nums []int
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{nums: []int{}}
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	this.nums = append(this.nums, x)
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	endIndex := len(this.nums) - 1
	num := this.nums[endIndex]
	this.nums = this.nums[:endIndex]
	return num
}

/** Get the top element. */
func (this *MyStack) Top() int {
	endIndex := len(this.nums) - 1
	if endIndex < 0 {
		return 0
	}
	return this.nums[endIndex]
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return len(this.nums) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

func main() {
	obj := Constructor()
	obj.Push(3)
	fmt.Println("3 -> ", obj.Pop())
	fmt.Println("nil -> ", obj.Top())
	fmt.Println("true ->", obj.Empty())
}
