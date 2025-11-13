import numpy as np

a = np.array([[1, 1],
              [1, 2]])

# 행렬식
print(np.linalg.det(a))

print()

# 역행렬
print(np.linalg.inv(a))
