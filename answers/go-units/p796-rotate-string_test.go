package leetcode

import "testing"

func Test_rotateString(t *testing.T) {
	type args struct {
		A string
		B string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"e1", args{"abcde", "cdeab"}, true},
		{"e2", args{"abcde", "abced"}, false},
		{"t1", args{"ab", "ba"}, true},
		{"t1", args{"ab", "bc"}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rotateString(tt.args.A, tt.args.B); got != tt.want {
				t.Errorf("rotateString() = %v, want %v", got, tt.want)
			}
		})
	}
}
