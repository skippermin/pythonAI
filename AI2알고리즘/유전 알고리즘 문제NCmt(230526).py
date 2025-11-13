from random import *


def decode(x):

    tens = 0
    
    for i in range(4):
        
        if x[i] == '1':
            tens = tens + (2 ** (3 - i)) 
        
    return tens


def fitness(x):
    return (x * 15) - (x ** 2)



X = []
decodeX = []
fitX = []
fitperX = []
fitperDescX = []
descindex = []
gene = 1

fit_set = 10

cross = 0.7
mutat = 0.001


for i in range(6):
    lineStr = []
    linedecode = []
    linefit = []
    linefitper = []
    fitperDescX.append(0)
    descindex.append(0)
    
    for j in range(fit_set):
        lineStr.append('')
        linedecode.append(0)
        linefit.append(0)
        linefitper.append(0)
    
    X.append(lineStr)
    decodeX.append(linedecode)
    fitX.append(linefit)
    fitperX.append(linefitper)
    

X[0][0] = '1100'
X[1][0] = '0100'
X[2][0] = '0001'
X[3][0] = '1110'
X[4][0] = '0111'
X[5][0] = '1001'


fitsum = 0

for i in range(6):
    decodeX[i][0] = decode(X[i][0])
    fitX[i][0] = fitness(decodeX[i][0])
    fitsum = fitsum + fitX[i][0]


for i in range(6):
    per = (fitX[i][0] * 100) / fitsum
    fitperX[i][0] = int(per)
    fitperDescX[i] = int(per)
    descindex[i] = i

for i in range(0, 5):

    for j in range((i + 1), 6):
        if fitperDescX[i] < fitperDescX[j]:
            temp = fitperDescX[i]
            fitperDescX[i] = fitperDescX[j]
            fitperDescX[j] = temp

            temp = descindex[i]
            descindex[i] = descindex[j]
            descindex[j] = temp
            

print(gene, "세대 염색체 적합도", sep = '')
for i in descindex:
    print("<X", (i + 1), gene, " ", X[i][0], " ", decodeX[i][0], " 적합도 ", fitX[i][0], " 적합도 비율 ", fitperX[i][0], ">"
          , end = '  ', sep = '')
                

print("\n\n")


sum_per = 0.0
index_1 = 0
index_2 = 0

while fit_set != gene:

    count = 0
    while count != 6:

        rand = uniform(0.0, cross + mutat)
        
        if rand > mutat:

            index_1 = 0
            index_2 = 0

            sum_per = 0.0
           

            while index_1 == index_2:

                for i in range(6):
                    sum_per = sum_per + fitperX[i][(gene - 1)]

                rand_1 = uniform(0.0, sum_per)
                rand_2 = uniform(0.0, sum_per)
        
                sum_per = 0.0

                for i in range(6):
                    sum_per = sum_per + fitperX[i][(gene - 1)]

                    if rand_1 <= sum_per:
                        index_1 = i
                        break

                sum_per = 0.0

                for i in range(6):
                    sum_per = sum_per + fitperX[i][(gene - 1)]

                    if rand_2 <= sum_per:
                        index_2 = i
                        break
                    

            crossX_1 = list(X[index_1][(gene - 1)])
            crossX_2 = list(X[index_2][(gene - 1)])

            cross_min = len(crossX_1) - round(len(crossX_1) * cross)
            cross_max = len(crossX_1)

            for i in range(cross_min, cross_max):
                temp = crossX_1[i]
                crossX_1[i] = crossX_2[i]
                crossX_2[i] = temp

            for i in range(6):
                if X[i][gene] == "".join(crossX_1):
                    index_1 = -1
                    break

            for i in range(6):
                if X[i][gene] == "".join(crossX_2):
                    index_2 = -1
                    break

            if (index_1 != -1) and (count != 6):
                X[count][gene] = "".join(crossX_1)
                count = count + 1

            if (index_2 != -1) and (count != 6):
                X[count][gene] = "".join(crossX_2)
                count = count + 1

        else:

            for i in range(6):
                sum_per = sum_per + fitperX[i][(gene - 1)]

            rand_1 = uniform(0.0, sum_per)
            sum_per = 0.0

            for i in range(6):
                sum_per = sum_per + fitperX[i][(gene - 1)]

                if rand_1 <= sum_per:
                    index_1 = i
                    break
                
            crossX_1 = list(X[index_1][(gene - 1)])
            
            temp = crossX_1[0]
            crossX_1[0] = crossX_1[1]
            crossX_1[1] = temp

            X[count][gene] = "".join(crossX_1)

            count = count + 1


    fitsum = 0

    for i in range(6):
        decodeX[i][gene] = decode(X[i][gene])
        fitX[i][gene] = fitness(decodeX[i][gene])
        fitsum = fitsum + fitX[i][gene]

    for i in range(6):
        per = (fitX[i][gene] * 100) / fitsum
        fitperX[i][gene] = int(per)
        fitperDescX[i] = int(per)
        descindex[i] = i

    for i in range(0, 5):
        for j in range((i + 1), 6):
            if fitperDescX[i] < fitperDescX[j]:
                temp = fitperDescX[i]
                fitperDescX[i] = fitperDescX[j]
                fitperDescX[j] = temp

                temp = descindex[i]
                descindex[i] = descindex[j]
                descindex[j] = temp

    print((gene + 1), "세대 염색체 적합도", sep = '')
    for i in descindex:
        print("<X", (i + 1), (gene + 1), " ", X[i][gene], " ", decodeX[i][gene], " 적합도 " ,fitX[i][gene]
              , " 적합도 비율 ", fitperX[i][gene], ">", end = '  ', sep = '')
            
    print("\n\n")
    

    gene = gene + 1
