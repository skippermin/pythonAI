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

plt.annotate('{0}'.format(RootNode) ,xy=(37.3,107),xytext=(49.5,134.6), color = 'black', fontsize='30', arrowprops = dict(arrowstyle="-",linewidth = 5,color='black'))
plt.annotate('' ,xy=(64.4,107),xytext=(51.4,134.3), color = 'black', fontsize='30', arrowprops = dict(arrowstyle="-",linewidth = 5,color='black'))
plt.annotate('O',(41,125),fontsize='20')
plt.annotate('Good',(34.2,99),fontsize='30')
plt.show()

K_2 = [1,0,0,0]

A_2 = [1.,1.,0.,0.]

B_2 = [1.,0.,1.,0.]

EntropySSox = round((-(1/4) * math.log2(1/4)) + (-(3/4) * math.log2(3/4)),6)

EntropyASSo = round((-(1/2) * math.log2(1/2)) + (-(1/2) * math.log2(1/2)), 6)
EntropyASSx = round(0 + (-(2/2) * math.log2(2/2)),6)
GainSSA = round(EntropySSox +(-(2/4)*EntropyASSo) + (-(2/4)*EntropyASSx),6)

EntropyBSSo = round((-(1/2) * math.log2(1/2)) + (-(1/2) * math.log2(1/2)), 6)
EntropyBSSx = round(0 + (-(2/2) * math.log2(2/2)),6)
GainSSB = round(EntropySSox +(-(2/4)*EntropyBSSo) + (-(2/4)*EntropyBSSx),6)

print("GainSSA : ",GainSSA)
print("GainSSB : ",GainSSB)

if(GainSSA>GainSSB):
    Childnode='A'
elif(GainSSB>GainSSA):
    Childnode='B'
elif(GainSSB==GainSSA):
    Childnode='B'

K_3 = [1,0]

ASSSo = [1]
ASSSx = [0]

plt.axis([0,100,0,150])

plt.annotate('{0}'.format(RootNode) ,xy=(37.3,107),xytext=(49.5,134.6), color = 'black', fontsize='30', arrowprops = dict(arrowstyle="-",linewidth = 5,color='black'))
plt.annotate('' ,xy=(64.4,107),xytext=(51.4,134.3), color = 'black', fontsize='30', arrowprops = dict(arrowstyle="-",linewidth = 5,color='black'))
plt.annotate('O',(41,125),fontsize='20')
plt.annotate('Good',(34.2,99),fontsize='30')

plt.annotate('{0}'.format(Childnode), xy=(74.7,71.7), xytext=(64.7,99.6),color = 'black', fontsize='30', arrowprops = dict(arrowstyle="-",linewidth = 5,color='black'))
plt.annotate('',xy=(56.4,71.7),xytext=(64.5,99.2),arrowprops = dict(color='black',linewidth = 5,arrowstyle="-"))

plt.annotate('Bad',(74.2,66.1),fontsize='30')
plt.annotate('O',(57.3,82),fontsize='20')
plt.annotate('X',(72.3,82),fontsize='20')

plt.annotate('A', xy=(48,39.3), xytext=(54.7,66.2),color = 'black', fontsize='30', arrowprops = dict(arrowstyle="-",linewidth = 5,color='black'))
plt.annotate('',xy=(60.7,39.4),xytext=(55.2,65.2),arrowprops = dict(color='black',linewidth = 5,arrowstyle="-"))

plt.annotate('Good',(45.2,33.5),fontsize='30')
plt.annotate('O',(48.5,47.5),fontsize='20')

plt.annotate('Bad',(60.5,33.5),fontsize='30')
plt.annotate('X',(60.5,47.5),fontsize='20')
plt.show()
