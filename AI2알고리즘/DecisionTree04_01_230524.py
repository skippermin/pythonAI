import matplotlib.pyplot as plt
import math

plt.axis([0,100,0,150])

K = [1.,1.,1.,1.,1.,0.,0.,0.]

C = [1.,1.,1.,1.,0.,0.,0.,0.]

B = [1.,0.,1.,0.,1.,0.,1.,0.]

A = [1.,1.,0.,0.,1.,1.,0.,0.]


EntropySox = round((-(5/8) * math.log2(5/8)) + (-(3/8) * math.log2(3/8)),6)

EntropyCSo = round((-(4/4) * math.log2(4/4)) + 0, 6)
EntropyCSx = round((-(1/4) * math.log2(1/4)) + (-(3/4) * math.log2(3/4)),6)
GainSC = round(EntropySox +(-(4/8)*EntropyCSo) + (-(4/8)*EntropyCSx),6)

EntropyBSo = round((-(3/4) * math.log2(3/4)) + (-(1/4) * math.log2(1/4)), 6)
EntropyBSx = round((-(2/4) * math.log2(2/4)) + (-(2/4) * math.log2(2/4)),6)
GainSB = round(EntropySox +(-(4/8)*EntropyBSo) + (-(4/8)*EntropyBSx),6)

EntropyASo = round((-(3/4) * math.log2(3/4)) + (-(1/4) * math.log2(1/4)), 6)
EntropyASx = round((-(2/4) * math.log2(2/4)) + (-(2/4) * math.log2(2/4)),6)
GainSA = round(EntropySox +(-(4/8)*EntropyBSo) + (-(4/8)*EntropyBSx),6)

print("GainSA : ",GainSA)
print("GainSB : ",GainSB)
print("GainSC : ",GainSC)

if(GainSA>GainSB and GainSA>GainSC):
    RootNode = "A"
elif(GainSB>GainSA and GainSB>GainSC):
    RootNode = "B"
elif(GainSC>GainSA and GainSC>GainSB):
    RootNode = "C"

plt.annotate('{0}'.format(RootNode) ,xy=(37.3,107),xytext=(49.5,134.6), color = 'black', fontsize='10', arrowprops = dict(arrowstyle="-",linewidth = 3,color='black'))
plt.annotate('' ,xy=(64.4,107),xytext=(51.4,134.3), color = 'black', fontsize='10', arrowprops = dict(arrowstyle="-",linewidth = 3,color='black'))
plt.annotate('O',(41,125),fontsize='10')
plt.annotate('Good',(34.2,99),fontsize='10')
plt.show()


