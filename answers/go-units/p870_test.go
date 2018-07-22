package leetcode

import (
	"reflect"
	"testing"
)

func Test_advantageCount(t *testing.T) {
	type args struct {
		A []int
		B []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"e1", args{[]int{2, 7, 11, 15}, []int{1, 10, 4, 11}}, []int{2, 11, 7, 15}},
		{"e2", args{[]int{12, 24, 8, 32}, []int{13, 25, 32, 11}}, []int{24, 32, 8, 12}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := advantageCount(tt.args.A, tt.args.B); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("advantageCount() = %v, want %v", got, tt.want)
			}
		})
	}
}
