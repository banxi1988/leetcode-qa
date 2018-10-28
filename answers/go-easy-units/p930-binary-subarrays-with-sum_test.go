package geasy

import "testing"

func Test_numSubarraysWithSum(t *testing.T) {
	type args struct {
		A []int
		S int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"t1", args{[]int{1, 0, 1, 0, 1}, 2}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numSubarraysWithSum(tt.args.A, tt.args.S); got != tt.want {
				t.Errorf("numSubarraysWithSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
