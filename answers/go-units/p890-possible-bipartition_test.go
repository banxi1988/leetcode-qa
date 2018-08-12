package leetcode

import "testing"

func Test_possibleBipartition(t *testing.T) {
	type args struct {
		N        int
		dislikes [][]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"e1", args{4, [][]int{{1, 2}, {1, 3}, {2, 4}}}, true},
		{"e2", args{3, [][]int{{1, 2}, {1, 3}, {2, 3}}}, false},
		{"e3", args{5, [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {1, 5}}}, false},
		{"e4", args{10, [][]int{{4, 7}, {4, 8}, {2, 8}, {8, 9}, {1, 6}, {5, 8}, {1, 2}, {6, 7}, {3, 10}, {8, 10}, {1, 5}, {7, 10}, {1, 10}, {3, 5}, {3, 6}, {1, 4}, {3, 9}, {2, 3}, {1, 9}, {7, 9}, {2, 7}, {6, 8}, {5, 7}, {3, 4}}}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := possibleBipartition(tt.args.N, tt.args.dislikes); got != tt.want {
				t.Errorf("possibleBipartition() = %v, want %v", got, tt.want)
			}
		})
	}
}
