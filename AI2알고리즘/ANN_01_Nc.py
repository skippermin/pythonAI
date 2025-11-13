#---고정 값---
alpha = 0.1 #학습률 
theta = 0.2 #임계치 

x_1 = 1 #3번째 데이터의 x_1의 입력 값
x_2 = 0 #3번째 데이터의 x_2의 입력 값

y_d = 0 #3번째 데이터의 정답(목표) 값

x_1_weight = 0.3 #x_1의 가중치
x_2_weight = -0.1 #x_2의 가중치

print("Epoch\tx1\tx2\ty_d(목표)\t\tx_1가중치\t\tx_2가중치\t\tY_out(실제 예측 값)\t\tY_pred(예측 출력 값)\t\tError(에러)\t최종x_1가중치\t최종x_2가중치")

Y_out = ((x_1*x_1_weight)+(x_2*x_2_weight)-theta)
#(x_1입력 값 * x_1입력 값의 가중치)+(x_2입력 값 * x_2입력 값의 가중치)-임계치 
#Y_out = (1*0.3)+(0*-0.1)+(-0.2) = 0.1
#모델이 예측한 값은 0.1
if Y_out >= 0:
    y_pred = 1 #모델이 예측한 출력 값을 1로 설정
    #y_pred = 실제 예측 값
else:#그렇지 않다면
    y_pred = 0 #모델이 예측한 출력 값을 0으로 설정
    #y_pred = 실제 예측 값
Error = y_d - y_pred
#에러 판별 = 정답(목표) 값 - 실제 예측 값
#Error = 0 - 1 = -1
print("\t",x_1,"\t",x_2,"\t",y_d,"\t\t",x_1_weight,"\t\t",x_2_weight,"\t\t",round(Y_out,1),"\t\t\t",y_pred,"\t\t\t",Error,'\t\t',end='')

x_1_weight = round(x_1_weight + alpha * x_1 * Error,1)

x_2_weight = round(x_2_weight + alpha * x_2 * Error,1)

print(x_1_weight,"      \t \t",x_2_weight)
