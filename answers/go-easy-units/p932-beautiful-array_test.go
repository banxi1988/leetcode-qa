package geasy

import (
	"reflect"
	"testing"
)

func Test_beautifulArray(t *testing.T) {
	type args struct {
		N int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"t1", args{4}, []int{2, 1, 4, 3}},
		{"t2", args{5}, []int{3, 1, 2, 5, 4}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := beautifulArray(tt.args.N); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("beautifulArray() = %v, want %v", got, tt.want)
			}
		})
	}
}
