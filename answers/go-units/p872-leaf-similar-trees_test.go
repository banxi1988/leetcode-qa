package leetcode

import "testing"

func Test_leafSimilar(t *testing.T) {

	root := &TreeNode{Val: 3}
	root.Left = &TreeNode{Val: 5}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2}
	root.Left.Right.Left = &TreeNode{Val: 7}
	root.Left.Right.Right = &TreeNode{Val: 4}

	root.Right = &TreeNode{Val: 1}
	root.Right.Left = &TreeNode{Val: 9}
	root.Right.Right = &TreeNode{Val: 8}

	root2 := &TreeNode{Val: 3}
	root2.Left = &TreeNode{Val: 5}
	root2.Right = &TreeNode{Val: 1}

	root2.Left.Left = &TreeNode{Val: 6}
	root2.Left.Right = &TreeNode{Val: 7}
	root2.Right.Left = &TreeNode{Val: 4}
	root2.Right.Right = &TreeNode{Val: 2}
	root2.Right.Right.Left = &TreeNode{Val: 9}
	root2.Right.Right.Right = &TreeNode{Val: 8}

	type args struct {
		root1 *TreeNode
		root2 *TreeNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"t1", args{root, root2}, true},
		{"t2", args{&TreeNode{Val: 1}, &TreeNode{Val: 2}}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := leafSimilar(tt.args.root1, tt.args.root2); got != tt.want {
				t.Errorf("leafSimilar() = %v, want %v", got, tt.want)
			}
		})
	}
}
