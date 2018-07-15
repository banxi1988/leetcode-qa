package leetcode

import "testing"

func Test_reorderedPowerOf2(t *testing.T) {
	type args struct {
		N int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"1", args{1}, true},
		{"2", args{2}, true},
		{"4", args{4}, true},
		{"10", args{10}, false},
		{"16", args{16}, true},
		{"24", args{24}, false},
		{"23", args{23}, true},
		{"46", args{46}, true},
		{"1521", args{1521}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reorderedPowerOf2(tt.args.N); got != tt.want {
				t.Errorf("reorderedPowerOf2() = %v, want %v", got, tt.want)
			}
		})
	}
}
