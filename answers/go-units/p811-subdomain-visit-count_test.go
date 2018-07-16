package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_subdomainVisits(t *testing.T) {
	type args struct {
		cpdomains []string
	}
	cpdomains1 := []string{"9001 discuss.leetcode.com"}
	cpdomains2 := []string{"900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{"e1", args{cpdomains1}, []string{"9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"}},
		{"e2", args{cpdomains2}, []string{"901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := subdomainVisits(tt.args.cpdomains)
			assert.ElementsMatch(t, got, tt.want)
		})
	}
}
