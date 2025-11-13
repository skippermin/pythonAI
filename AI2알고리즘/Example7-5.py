import numpy as np
import matplotlib.pyplot as plt

# -- 입력과 정답의 준비 --
X = np.linspace(-np.pi/2, np.pi/2)  # 입력: -π/2부터 π/2 미만의 범위
T = (np.sin(X) + 1)/2  # 정답: 0부터 1의 범위
n_data = len(T)  # 데이터 수

# --- 그래프로 그려본다 ---
plt.plot(X, T)

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()

plt.show()
