package geasy

import "testing"
import "github.com/stretchr/testify/assert"

func Test_numUniqueEmails(t *testing.T) {
	arr1 := []string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}
	r1 := numUniqueEmails(arr1)
	assert.Equal(t, 2, r1)

}

func Test_normalizeLocalName(t *testing.T) {
	assert.Equal(t, "testemail", normalizeLocalName("test.email"))
	assert.Equal(t, "testemail", normalizeLocalName("test.email+test"))
}

func Test_normalizeEmail(t *testing.T) {
	assert.Equal(t, "testemail@leetcode.com", normalizeEmail("test.email+alex@leetcode.com"))
}
