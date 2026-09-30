import numpy as np
import math
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
  new_arr= np.array(a)
  if math.prod(new_shape) != new_arr.size:
    reshaped_matrix = []
  else:
   reshape_arr = new_arr.reshape(new_shape)
   reshaped_matrix = reshape_arr.tolist()
  return reshaped_matrix