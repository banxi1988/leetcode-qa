package leetcode

import "testing"

func Test_toLowerCase(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"e1", args{"Hello"}, "hello"},
		{"e2", args{"here"}, "here"},
		{"e3", args{"LOVELY"}, "lovely"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := toLowerCase(tt.args.str); got != tt.want {
				t.Errorf("toLowerCase() = %v, want %v", got, tt.want)
			}
		})
	}
}
