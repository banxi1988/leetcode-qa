package main

import "fmt"

type MyQueue struct {
	nums []int
}

/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{nums: []int{}}
}

/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	this.nums = append(this.nums, x)
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	num := this.nums[0]
	this.nums = this.nums[1:]
	return num
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	return this.nums[0]
}

/** Returns whether the stack is empty. */
func (this *MyQueue) Empty() bool {
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
	obj.Push(2)
	fmt.Println("3 -> ", obj.Pop())
	fmt.Println("2 -> ", obj.Peek())
	fmt.Println("false ->", obj.Empty())
}
