import random

A = 10
B = 20
C = 30
D = 40
G1 = 0
G2 = 0
p = 0
print("Crossover")
for i in range(0,1,1):
    rand = random.randint(1, 100)
    print("첫번째 난수 값 : ",rand)
    t = A + B + C + D
    p += A
    if rand <= p:
        G1 = 'A'
        break;
    p += B
    if rand <= p:
        G1 = 'B'
        break
    p += C
    if rand <= p:
        G1 = 'C'
        break
    p += D
    if rand <= p:
        G1 = 'D'
        break
print('G1 :', G1)
for i in range(0,1,1):
    rand = random.randint(1, 100)
    print("두번째 난수 값 : ",rand)
    p += A
    if rand <= p and G1 != 'A':
        G2 = 'A'
        break
    p += B
    if rand <= p and G1 != 'B':
        G2 = 'B'
        break
    p += C
    if rand <= p and G1 != 'C':
        G2 = 'C'
        break
    p += D
    if rand <= p and G1 != 'D':
        G2 = 'D'
        break
print('G2 :', G2)
print('결과 G1 :', G1, ',G2 :', G2,)
