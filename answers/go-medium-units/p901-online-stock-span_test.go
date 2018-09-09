package gmedium

import "testing"
import "github.com/stretchr/testify/assert"

func TestStockSpanner_Next(t *testing.T) {
	s1 := StockSpannerConstructor()
	assert.Equal(t, 1, s1.Next(100))
	assert.Equal(t, 1, s1.Next(80))
	assert.Equal(t, 1, s1.Next(60))
	assert.Equal(t, 2, s1.Next(70))
	assert.Equal(t, 1, s1.Next(60))
	assert.Equal(t, 4, s1.Next(75))
	assert.Equal(t, 6, s1.Next(85))
}
