package gmedium

import "testing"

func Test_knightDialer(t *testing.T) {
	type args struct {
		N int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{1}, 10},
		{"2", args{2}, 20},
		{"3", args{3}, 46},
		{"18", args{18}, 46},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := knightDialer2(tt.args.N); got != tt.want {
				t.Errorf("knightDialer() = %v, want %v", got, tt.want)
			}
		})
	}
}
