package gmedium

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_fourSum(t *testing.T) {
	// e1 := [][]int{{-1, 0, 0, 1}, {-2, -1, 1, 2}, {-2, 0, 0, 2}}
	// assert.ElementsMatch(t, e1, fourSum([]int{1, 0, -1, 0, -2, 2}, 0))

	e2 := [][]int{{-5, -4, -3, 1}}
	assert.ElementsMatch(t, e2, fourSum([]int{1, -2, -5, -4, -3, 3, 3, 5}, -11))
}
