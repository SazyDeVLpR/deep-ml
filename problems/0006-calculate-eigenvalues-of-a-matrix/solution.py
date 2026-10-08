import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = np.array(matrix)
	ev = np.linalg.eigvals(a)
	eigenvalues = ev.real.astype(float)
	return eigenvalues