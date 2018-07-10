package leetcode

import "testing"

func Test_rotatedDigits(t *testing.T) {
	type args struct {
		N int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"2", args{2}, 1},
		{"5", args{5}, 2},
		{"10", args{10}, 4},
		{"11", args{11}, 4},
		{"12", args{12}, 5},
		{"15", args{15}, 6},
		{"16", args{16}, 7},
		{"18", args{18}, 7},
		{"19", args{19}, 8},
		{"20", args{20}, 9},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rotatedDigits(tt.args.N); got != tt.want {
				t.Errorf("rotatedDigits() = %v, want %v", got, tt.want)
			}
		})
	}
}
