# 유전 알고리즘 코딩을 하는 문제를 제출하시오.
import random
import copy

rand = random.randint(1, 100)

A = 10
B = 20
C = 30
D = 40
G1 = 0
p = 0

print("Mutation")
print("난수 값 : " , rand)
for i in range(0,1,1):
    t = A + B + C + D
    p += A
    if rand <= p:
        G1 = "A"
        print("G1 :", G1)
        break
    p += B
    if rand <= p:
        G1 = "B"
        print("G1 :", G1)
        break
    p += C
    if rand <= p:
        G1 = "C"
        print("G1 :", G1)
        break
    p += D
    if rand <= p:
        G1 = "D"
        print("G1 :", G1)
        break
