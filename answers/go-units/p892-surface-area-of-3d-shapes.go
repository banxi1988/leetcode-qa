package leetcode

func surfaceArea(grid [][]int) int {
	N := len(grid)
	totalArea := 0
	preLevelCells := 0

	calcCellEdgeArea := func(i, j int) int {
		area := 4
		if j > 0 && grid[i][j-1] > 0 {
			area--
		}
		if j < N-1 && grid[i][j+1] > 0 {
			area--
		}
		if i > 0 && grid[i-1][j] > 0 {
			area--
		}
		if i < N-1 && grid[i+1][j] > 0 {
			area--
		}
		return area
	}

	for level := 1; level < 52; level++ {
		levelEdgeArea := 0
		levelCells := 0
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				cellLevels := grid[i][j]
				if cellLevels > 0 {
					cellEdgeArea := calcCellEdgeArea(i, j)
					levelEdgeArea += cellEdgeArea
					levelCells++
				}
			}
		}
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				cellLevels := grid[i][j]
				if cellLevels > 0 {
					grid[i][j] = cellLevels - 1
				}
			}
		}

		if preLevelCells > 0 {
			topSurfaceArea := preLevelCells - levelCells
			totalArea += topSurfaceArea
		} else {
			totalArea += levelCells // 底面积
		}
		totalArea += levelEdgeArea
		preLevelCells = levelCells
		if levelCells < 1 {
			break
		}

	}
	return totalArea
}
