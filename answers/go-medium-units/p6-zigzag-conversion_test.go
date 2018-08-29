package gmedium

import "testing"
import "github.com/stretchr/testify/assert"

func Test_convert(t *testing.T) {
	assert.Equal(t, "AB", convert("AB", 1))
	assert.Equal(t, "PAHNAPLSIIGYIR", convert("PAYPALISHIRING", 3))
	assert.Equal(t, "PINALSIGYAHRPI", convert("PAYPALISHIRING", 4))
}
