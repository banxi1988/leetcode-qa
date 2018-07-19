package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_shortestToChar(t *testing.T) {
	type args struct {
		S string
		C byte
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"e1", args{"loveleetcode", 'e'}, []int{3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0}},
	}
	fmt.Println("slice ", []int{1,2,3,4}[0:1])
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := shortestToChar(tt.args.S, tt.args.C)
			assert.Equal(t, got, tt.want)
		})
	}
}
