print("------------------------------")
print("이름: 장민우")
print("소속: 융합소프트웨어학부 응용소프트웨어전공")
print("학번: 60161628")
print("------------------------------")

# NumPy 라이브러리를 가져옵니다.
import numpy as np

# 시그모이드 함수를 정의합니다.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# AND 연산을 구현합니다.
def and_gate(x1, x2):
    # AND 연산의 진리표를 통해 가중치와 편향을 구합니다.
    w1 = 1
    w2 = 1
    b = 0.5

    # 입력값을 곱한 후 가중치와 편향을 더합니다.
    y = sigmoid(x1 * w1 + x2 * w2 + b)

    # 출력값을 반환합니다.
    return y

# OR 연산을 구현합니다.
def or_gate(x1, x2):
    # OR 연산의 진리표를 통해 가중치와 편향을 구합니다.
    w1 = 1
    w2 = 1
    b = 0.5

    # 입력값을 곱한 후 가중치와 편향을 더합니다.
    y = sigmoid(x1 * w1 + x2 * w2 + b)

    # 출력값을 반환합니다.
    return y

# NOT 연산을 구현합니다.
def not_gate(x):
    # NOT 연산의 진리표를 통해 가중치와 편향을 구합니다.
    w1 = 1
    b = 0.5

    # 입력값을 곱한 후 가중치와 편향을 더합니다.
    y = sigmoid(x * w1 + b)

    # 출력값을 반환합니다.
    return y

# 각 연산에 대해 입력값을 주어 출력값을 계산합니다.
print(and_gate(0, 0))
print(and_gate(0, 1))
print(and_gate(1, 0))
print(and_gate(1, 1))

print(or_gate(0, 0))
print(or_gate(0, 1))
print(or_gate(1, 0))
print(or_gate(1, 1))

print(not_gate(0))
print(not_gate(1))