package leetcode

import "testing"

func Test_largestTriangleArea(t *testing.T) {
	type args struct {
		points [][]int
	}
	tests := []struct {
		name string
		args args
		want float64
	}{
		{"e1", args{[][]int{{0, 0}, {0, 1}, {1, 0}, {0, 2}, {2, 0}}}, 2},
		{"e2", args{[][]int{{4, 6}, {6, 5}, {3, 1}}}, 5.5},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestTriangleArea(tt.args.points); got != tt.want {
				t.Errorf("largestTriangleArea() = %v, want %v", got, tt.want)
			}
		})
	}
}
