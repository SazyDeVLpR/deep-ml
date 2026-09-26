import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	np_matrix= np.array(matrix)
	out= scalar*np_matrix
	return out.tolist()
	pass