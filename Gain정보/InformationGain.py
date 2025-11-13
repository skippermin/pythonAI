print("이름: 장민우")
print("학번: 60161628")
import math
## Information Gain
## C속성에 대한 데이터 출력

EntropySox = (-(5/8) * math.log2(5/8)) + (-(3/8) * math.log2(3/8))
EntropyCSo = (-(4/4) * math.log2(4/4)) + 0
EntropyCSx = (-(1/4) * math.log2(1/4)) + (-(3/4) * math.log2(3/4))
GainSC = EntropySox +(-(4/8)*EntropyCSo) + (-(4/8)*EntropyCSx)
print("EntropySox = ",round(EntropySox,6))
print("EntropyCSo = ",round(EntropyCSo,6))
print("EntropyCSx = ",round(EntropyCSx,6))
print("GainSC = ",round(GainSC,6))


