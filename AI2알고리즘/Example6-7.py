import numpy as np
import matplotlib.pyplot as plt

p = np.array([0.75, 0.23, 0.02])  # 확률
x = np.array([100, 500, 10000])  # 값

# 기댓값
print(np.sum(p*x))
