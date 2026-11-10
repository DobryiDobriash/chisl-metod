import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print(a.shape)   # (3, 4)
print(a.ndim)    # 2
print(a.size)    # 12
print(a.dtype)   # int64