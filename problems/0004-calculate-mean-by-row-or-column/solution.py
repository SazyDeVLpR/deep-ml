import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	npmatrix = np.array(matrix)
	colmatrix = []
	rowmatrix = []
	rows, columns = npmatrix.shape
	if mode == "row":
		for i in range(rows):
			total = 0
			for j in range(columns):
				total += matrix[i][j]
			rowmean = total/columns
			rowmatrix.append(rowmean)
		means = rowmatrix
	else:
		for j in range(columns):
			total = 0
			for i in range(rows):
				total += matrix[i][j]
			colmean = total/rows
			colmatrix.append(colmean)
		means = colmatrix
	return means