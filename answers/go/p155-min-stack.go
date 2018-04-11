package main

import "fmt"

//// BEGIN
type Node struct {
	Num        int
	CurrentMin int
}

type MinStack struct {
	Elems []Node
}

/* initialize your data structure here. */
func Constructor() MinStack {
	stack := MinStack{Elems: []Node{}}
	return stack
}

func (this *MinStack) Push(x int) {
	elemCount := len(this.Elems)
	if elemCount == 0 {
		node := Node{x, x}
		this.Elems = append(this.Elems, node)
	} else {
		prevNode := this.Elems[len(this.Elems)-1]
		currentMin := prevNode.CurrentMin
		if x < currentMin {
			currentMin = x
		}
		node := Node{x, currentMin}
		this.Elems = append(this.Elems, node)
	}
}

func (this *MinStack) Pop() {
	this.Elems = this.Elems[:len(this.Elems)-1]
}

func (this *MinStack) Top() int {
	node := this.Elems[len(this.Elems)-1]
	return node.Num
}

func (this *MinStack) GetMin() int {
	node := this.Elems[len(this.Elems)-1]
	return node.CurrentMin
}

//// END

func main() {
	obj := Constructor()
	obj.Push(-2)
	obj.Push(0)
	obj.Push(-3)
	fmt.Println(" -3 -> ", obj.GetMin())
	obj.Pop()
	fmt.Println(" 0 -> ", obj.Top())
	fmt.Println(" -2 -> ", obj.GetMin())

}
