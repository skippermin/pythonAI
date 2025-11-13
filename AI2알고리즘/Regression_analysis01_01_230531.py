import matplotlib.pyplot as plt#matplotlib.pyplot 각각의 함수를 사용해서 간편하게 그래프를 만들고 변화 주는 모듈을 가져옴

x_data = [3.,10.,7.,9.,13.,11.]
y_data = [4.,11.,9.,13.,15.,9.]
#x,y데이터

new_data = 0
#new_data : 새롭게 들어오는 x데이터
#새롭게 들어온 x데이터를 가지고 y값을 예측하기 위함
new_data = float(input("새로운 데이터 = x값을 입력 :"))
#새로운 데이터 X = 6에 대한 종속변수 y의 추정 값을 구하기

y_pred = []
#y_pred : 독립 변수 x, 최적의 기울기, 절편 값의 데이터를 가지고 예측 값(y = ax + b)의 y값을 담기위해 만든 변수
#pred : predicted(예측)
y_new_data = 0
#y_new_data : 새로운 데이터(new_data) X = 6에 대한 종속변수 y값을 담기위해 만든 변수
a = 0.939727
#최적의 기울기(a) 값 : 0.939727
b = 1.86221059
#최적의 y절편(b) 값 : 1.86221059

plt.scatter(x_data,y_data, s=40)
#각각의 x, y 데이터를 이용해 산점도를 그리는데 사용된다.
#첫번째 인자 : x축에 해당하는 데이터 값(3,10,7,9,13,11)
#두번째 인자 : y축에 해당하는 데이터 값(4,11,9,13,15,9)
#세번째 인자 : 마커의 크기를 설정한다.

for i in range(6):#추정선을 그리기 위한 for문
    #데이터 개수 6만큼 반복한다. 
    y_pred.append(round(a*x_data[i]+b,6))
    #append() 함수를 이용해서 a * x_data[i] + b의 예측 값의 요소를 담는다.
    #예측 값 직선의 방정식 표현을 위한 y^ = ax+b의 y값을 담는다.
y_new_data = a*new_data+b
#새롭게 입력된 데이터에 대한 y의 추정 값을 y = ax+b로 저장한다.
print(y_pred)
plt.scatter(new_data,y_new_data)
#새로운 데이터 X = 6에 대한 종속변수 y의 추정 값
#scatter() 함수는 x, y 데이터를 이용해 산점도를 그리는데 사용된다.
plt.plot([min(x_data),max(x_data)],[min(y_pred),max(y_pred)])
#추세선을 표현하기 위해 만든 plot() 함수 
#첫번째 인자 : x축에 해당하는 데이터의 최소 값과 최대 값을 이용해서 그림을 나타냈다.
#x축에 해당하는 데이터(x_data)의 최소 값 : 3, x축에 해당하는 데이터(x_data)의 최대 값 : 13
#두번째 인자 : y축에 해당하는 데이터의 최소 값과 최대 값을 이용해서 그림을 나타냈다.
#x축에 해당하는 데이터(y_pred)의 최소 값 : 4.6, x축에 해당하는 데이터(y_pred)의 최대 값 : 14

#직선의 방정식의 표현을 위한 x값과 y값 표현
plt.xlabel('X')
#matplotlib.pyplot 모듈의 xlabel() 함수를 이용해 x축 라벨의 이름을 x로 지어주었다.
plt.ylabel('Y')
#matplotlib.pyplot 모듈의 ylabel() 함수를 이용해 y축 라벨의 이름을 y로 지어주었다.
plt.show()
#matplotlib.pyplot 모듈의 show() 함수는 그래프를 화면에 나타나도록 한다.
