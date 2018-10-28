package leetcode

import "testing"
import "github.com/stretchr/testify/assert"

func Test_FewestRmbExhcange(t *testing.T) {
	type args struct {
		amount int
	}
	tests := []struct {
		args args
		want []int
	}{
		{args{1}, []int{1}},
		{args{2}, []int{2}},
		{args{3}, []int{2, 1}},
		{args{4}, []int{2, 2}},
		{args{5}, []int{5}},
		{args{6}, []int{5, 1}},
		{args{7}, []int{5, 2}},
		{args{8}, []int{5, 2, 1}},
		{args{9}, []int{5, 2, 2}},
		{args{10}, []int{10}},
		{args{11}, []int{10, 1}},
		{args{12}, []int{10, 2}},
		{args{13}, []int{10, 2, 1}},
		{args{14}, []int{10, 2, 2}},
		{args{15}, []int{10, 5}},
		{args{16}, []int{10, 5, 1}},
		{args{17}, []int{10, 5, 2}},
		{args{100}, []int{100}},
		{args{103}, []int{100, 2, 1}},
		{args{200}, []int{100, 100}},
	}
	for _, tt := range tests {
		got := FewestRmbExhcange(tt.args.amount)
		assert.ElementsMatch(t, tt.want, got)
	}
}
