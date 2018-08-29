package gmedium

func convert(s string, numRows int) string {
	if numRows < 2 {
		return s
	}
	chars := []byte(s)
	charCount := len(chars)
	columns := [][]byte{}
	row := 0
	column := make([]byte, numRows)
	down := true
	for i := 0; i < charCount; i++ {
		column[row] = chars[i]
		if down {
			row++
		} else {
			row--
		}
		turn := false
		if row >= numRows {
			row = numRows - 2
			turn = true
		} else if row < 0 {
			row = 1
			turn = true
		}
		if turn {
			down = !down
			columns = append(columns, column)
			column = make([]byte, numRows)
		}

	}
	columns = append(columns, column)

	outchars := []byte{}
	for row := 0; row < numRows; row++ {
		for col := 0; col < len(columns); col++ {
			ch := columns[col][row]
			if ch != 0 {
				outchars = append(outchars, ch)
			}
		}
	}
	return string(outchars)
}
