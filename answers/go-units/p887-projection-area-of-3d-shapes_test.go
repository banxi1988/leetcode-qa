package leetcode

import "testing"

func Test_projectionArea(t *testing.T) {
	type args struct {
		grid [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"e1", args{[][]int{{2}}}, 5},
		{"e2", args{[][]int{{1, 2}, {3, 4}}}, 17},
		{"e1", args{[][]int{{1, 0}, {0, 2}}}, 8},
		{"e1", args{[][]int{{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}}, 14},
		{"e1", args{[][]int{{2, 2, 2}, {2, 1, 2}, {2, 2, 2}}}, 21},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := projectionArea(tt.args.grid); got != tt.want {
				t.Errorf("projectionArea() = %v, want %v", got, tt.want)
			}
		})
	}
}
