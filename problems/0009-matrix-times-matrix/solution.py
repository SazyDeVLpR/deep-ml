import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

 npa = np.array(a)
 npb = np.array(b)
 if np.shape(a)[1] != np.shape(b)[0]:
  return -1
 c = npa@npb
 return c