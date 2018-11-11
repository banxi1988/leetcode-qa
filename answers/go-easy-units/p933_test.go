package geasy

import "testing"
import "github.com/stretchr/testify/assert"

func TestRecentCounter_Ping(t *testing.T) {
	rc := Constructor()
	assert.Equal(t, 1,rc.Ping(642));
	assert.Equal(t, 2,rc.Ping(1849));
	assert.Equal(t, 1,rc.Ping(4921));
	assert.Equal(t, 2,rc.Ping(5936));
	assert.Equal(t, 3,rc.Ping(5957));
}
