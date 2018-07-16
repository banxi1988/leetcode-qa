package leetcode

import (
	"reflect"
	"testing"
)

func Test_numberOfLines(t *testing.T) {
	type args struct {
		widths []int
		S      string
	}
	widths1 := []int{10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}
	widths2 := []int{4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}

	tests := []struct {
		name string
		args args
		want []int
	}{
		{"e1", args{widths1, "abcdefghijklmnopqrstuvwxyz"}, []int{3, 60}},
		{"e2", args{widths2, "bbbcccdddaaa"}, []int{2, 4}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numberOfLines(tt.args.widths, tt.args.S); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("numberOfLines() = %v, want %v", got, tt.want)
			}
		})
	}
}
