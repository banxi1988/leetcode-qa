package leetcode

import "testing"

func Test_fewestRmbExhcange(t *testing.T) {
	type args struct {
		amount int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{1}, 1},
		{"2", args{2}, 2},
		{"3", args{3}, 3},
		{"4", args{4}, 4},
		{"5", args{5}, 1},
		{"6", args{6}, 2},
		{"7", args{7}, 3},
		{"8", args{8}, 4},
		{"9", args{9}, 5},
		{"10", args{10}, 1},
		{"11", args{11}, 2},
		{"12", args{12}, 3},
		{"13", args{13}, 4},
		{"14", args{14}, 5},
		{"15", args{15}, 2},
		{"16", args{16}, 3},
		{"17", args{17}, 4},
		{"100", args{100}, 1},
		{"103", args{103}, 4},
		{"200", args{200}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := fewestRmbExhcange(tt.args.amount); got != tt.want {
				t.Errorf("fewestRmbExhcange() = %v, want %v", got, tt.want)
			}
		})
	}
}
