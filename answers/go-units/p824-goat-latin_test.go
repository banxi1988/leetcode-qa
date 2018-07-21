package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_toGoatLatin(t *testing.T) {
	type args struct {
		S string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"e1", args{"I speak Goat Latin"}, "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"},
		{"e2", args{"The quick brown fox jumped over the lazy dog"}, "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"},
		{"e3", args{"Each word consists of lowercase and uppercase letters only"}, "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := toGoatLatin(tt.args.S)
			assert.Equal(t, tt.want, got)
		})
	}
}
