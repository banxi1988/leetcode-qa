package leetcode

import "testing"

func Test_mostCommonWord(t *testing.T) {
	type args struct {
		paragraph string
		banned    []string
	}
	para1 := "Bob hit a ball, the hit BALL flew far after it was hit."
	tests := []struct {
		name string
		args args
		want string
	}{
		{"e1", args{para1, []string{"hit"}}, "ball"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mostCommonWord(tt.args.paragraph, tt.args.banned); got != tt.want {
				t.Errorf("mostCommonWord() = %v, want %v", got, tt.want)
			}
		})
	}
}
