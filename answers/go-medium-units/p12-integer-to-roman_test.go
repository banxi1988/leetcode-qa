package gmedium

import "testing"
import "github.com/stretchr/testify/assert"

func Test_intToRoman(t *testing.T) {
	assert.Equal(t, "III", intToRoman(3))
	assert.Equal(t, "IV", intToRoman(4))
	assert.Equal(t, "IX", intToRoman(9))
	assert.Equal(t, "LVIII", intToRoman(58))
	assert.Equal(t, "MCMXCIV", intToRoman(1994))
}
