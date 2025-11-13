import matplotlib.pyplot as plt
#matplotlib.pyplot 각각의 함수를 사용해서 간편하게 그래프를 그리면서, 변화를 주는 라이브러리를 가져왔다.
import math
#수학적 함수를 이용하기 위한 math 라이브러리를 불러왔다.

#K-means 알고리즘
#K = 클러스터의 개수(나누는 갯수)
#이차원 평면에서 (1,1)  (2,2)  (3,3)  (7,7)  (8,8)  (9,9)를 가지고 두 개의 군집으로 나는 것을 파이썬으로 코딩
#중심값 두 개는 임의로 선정하고, 군집화가 되면 그래프로 군집에 따라 점들을 다른 색으로 표현
#처음엔 모두 검정색
#군집화가 되면 하나의 군집은 빨간색  다른 하나의 군집은 파란색으로 그래프에 표현

data = [[10.,20.,30.,70.,80.,90.],
        [10.,20.,30.,70.,80.,90.]]
#1번째 행에는 x_data의 값, 2번째 행에는 y_data의 값이 들어있다.


Class_A_Midian = [[0],[0]]
#임의로 정하기 위한 A클래스의 중심값을 선언과 동시에 (0, 0)으로 초기화 했다.
#A클래스의 중심값을 A클래스에 지정된 중심값을 이용하여 중심값과 데이터들의 거리를 측정하기 위함이다.

Class_B_Midian = [[0],[0]]
#임의로 정하기 위한 B클래스의 중심값을 선언과 동시에 (0, 0)으로 초기화 했다.
#B클래스의 중심값을 B클래스에 지정된 중심값을 이용하여 중심값과 데이터들의 거리를 측정하기 위함이다.

Class_A_Midian[0][0] = min(data[0])
Class_A_Midian[1][0] = min(data[1])
#A의 중심값은 (10, 10)으로 임의로 저장했다.
#data의 0번째 행의 벡터의 크기로 제일 작은 값을 찾아 저장했다.
Class_B_Midian[0][0] = max(data[0])
Class_B_Midian[1][0] = max(data[1])
#B의 중심값은 (90, 90)으로 임의로 저장했다.
#data의 1번째 행의 벡터의 크기로 제일 작은 값을 찾아 저장했다.
#최소값과 최대값으로 지정해 사용하는 이유 : 군집의 결과를 최대한 빨리 얻을 수 있기 때문이다.

prev_Class_A_Midian = [[10.],[10.]]
#A 중심값과 비교하기 위해 만들어진 이전의 중심값을 뜻하는 prev_class_A_midian을 선언과 동시에 (10, 10)으로 초기화 했다.
prev_Class_B_Midian = [[20.],[20.]]
#B 중심값과 비교하기 위해 만들어진 이전의 중심값을 뜻하는 prev_class_A_midian을 선언과 동시에 (10, 10)으로 초기화 했다.
#사용하는 이유 : 군집화 결과가 수렴할때 까지 반복적으로 이루어지기 때문이다. 

plt.plot(data[0],data[1],color='#000000',marker='o',markersize='12',linestyle='',label='data')
#초기의 데이터들을 보여주기 위해 만든 plot 그래프를 그려주었다.
#plt.plot(x값, y값, color = ‘16진수or색상’, marker = ‘마커의 종류‘, linestyle = ‘선의 종류’,
#markersize = ‘마커의 크기’, linewidth = ‘선의 굵기’, label = ‘그래프 라벨 이름’)
#1번째 인자 : x값의 데이터 위치
#2번째 인자 : y값의 데이터 위치
#3번째 인자 : 선의 색(검정색)
#4번째 인자 : 마커의 종류(o(원형 모양), ^(triangle_up(삼각형) 모양), s(정사각형 모양), p(오각형 모양),
#*(별 모양), h(육각형 모양), +(플러스 모양), d(다이아몬드 모양), _(언더바 모양))
#5번째 인자 : 선의 종류(‘-’: 실선 스타일,‘--’ : 파선 스타일,‘-.’ : Dash-Dot 선 스타일,
#‘:’ : 점선 스타일)
#6번째 인자 : 마커의 크기
#7번째 인자 : 선의 굵기
#8번째 인자 : 해당 선의 의미를 알려주는 라벨의 이름
#각각의 데이터들의 위치를 보여주고, 색은 검정색, 마커는 동그란원을 뜻하는 'o' 마커 사이즈는 3으로 설정하고 해당 데이터들의 라벨 이름을 'data'로 지어주었다. 
plt.legend(fontsize = '20')
#그래프의 라벨명을 출력하기 위해 쓰이는 legend() 함수
#그래프의 라벨의 크기를 '20'으로 설정하였다.
plt.title("set data")
#그래프의 타이틀 명을 보여주기 위해 쓰이는 title() 함수
plt.show()
#그래프를 화면에 보여주는 show() 함수이다.

plt.plot(data[0],data[1],color='#000000',marker='o',markersize='12',linestyle='',label='data')
#초기의 데이터들을 보여주기 위해 만든 plot 그래프를 그려주었다.
#각각의 데이터들의 위치를 보여주고, 색은 검정색, 마커는 동그란원을 뜻하는 'o' 마커 사이즈는 12으로 설정하고 해당 데이터들의 라벨 이름을 'data'로 지어주었다. 
plt.plot(Class_A_Midian[0],Class_A_Midian[1],color='#FF0000',marker='^',markersize='24',linestyle='',label='Class_A_Midian_data')
#초기의 Class_A의 중심 값을 보여주기 위해 만든 plot() 함수를 이용해 데이터를 그려주었다.
#각각의 데이터들의 위치를 보여주고, 색은 빨간색, 마커는 삼각형을 뜻하는 '^' 마커 사이즈는 24으로 설정하고 해당 데이터들의 라벨 이름을 'Class_A_Midian_data'로 지어주었다. 
plt.plot(Class_B_Midian[0],Class_B_Midian[1],color='#0000FF',marker='h',markersize='24',linestyle='',label='Class_B_Midian_data')
#초기의 Class_B의 중심 값을 보여주기 위해 만든 plot() 함수를 이용해 데이터를 그려주었다.
#각각의 데이터들의 위치를 보여주고, 색은 파란색, 마커는 육각형을 뜻하는 'h' 마커 사이즈는 24으로 설정하고 해당 데이터들의 라벨 이름을 'Class_B_Midian_data'로 지어주었다.
plt.legend(fontsize = '20')
#그래프의 라벨명을 출력하기 위해 쓰이는 legend() 함수
#그래프의 라벨의 크기를 '20'으로 설정하였다.
plt.title("Class_A_Midian, Class_B_Midian data")
#그래프의 타이틀 명을 보여주기 위해 쓰이는 title() 함수
plt.show()
#그래프를 화면에 보여주는 show() 함수이다.

for i in range(0,6,1):
#중심값과 데이터의 거리 계산과 데이터들의 평균을 이용하여 새로운 중심값 구하는 for문이다.
    A_eucliedean_distance_moem = [0,0,0,0,0,0]
    #A 중심값에 대한 데이터들의 거리를 초기화 해준다.
    #for문에서 사용하는 이유 : 중심값이 새롭게 업데이트 되어서, 중심값에 대한 데이터의 거리도 계속 바뀌기 때문에 새롭게 계속 초기화를 해주어야한다.
    B_eucliedean_distance_moem = [0,0,0,0,0,0]
    #B 중심값에 대한 데이터들의 거리를 초기화 해준다.
    Class_A = [[],[]]
    #Class_A에 속하는 데이터를 저장 위해 선언하였다.
    #각각 Class_A, B 중심값과 데이터들의 거리에 값들을 비교해서 Class_A 중심값과 가까운 데이터를 가져오기 위해 선언하였다. 
    Class_B = [[],[]]
    #Class_B에 속하는 데이터를 저장 위해 선언하였다.
    #각각 Class_A, B 중심값과 데이터들의 거리에 값들을 비교해서 Class_B 중심값과 가까운 데이터를 가져오기 위해 선언하였다. 
    
    for i in range(0,len(data[0]),1):
        # 중심 값과 데이터의 거리를 계산하고, 중심값과 가까운 거리의 데이터를 저장하기 위해 만들어진 for문
        # 데이터를 0(초기값)으로 시작해 6(조건)보다 작을때 까지 1(증감식) 늘려주는 for문 생성
        eucliedean_distance = math.sqrt((Class_A_Midian[0][0]-data[0][i])**2+(Class_A_Midian[1][0]-data[1][i])**2)
        # math.sqrt() 함수를 사용해 제곱근을 표현해주었다.
        # (Class_A의 x를 뜻하는 인덱스 [0][0]에 해당하는 중심 값 - 데이터의 x_data의 값)**2 + (Class_A의 y를 뜻하는 인덱스 [1][0]에 해당하는 중심 값 - 데이터의 y_data의 값)**2
        # A중심 값에 대한 여섯 번째 데이터의 좌표에 대한 유클리드 계산 :제곱근((7-9)^2+(7-9)^2)
        A_eucliedean_distance_moem[i] = eucliedean_distance
        # 각각의 데이터들의 유클리드 계산 결과 값을 A_eucliedean_distance_moem[i]번째 인덱스에 저장한다.
        eucliedean_distance = math.sqrt((Class_B_Midian[0][0]-data[0][i])**2+(Class_B_Midian[1][0]-data[1][i])**2)
        # math.sqrt() 함수를 사용해 제곱근을 표현해주었다.
        # (Class_B의 x를 뜻하는 인덱스 [0][0]에 해당하는 중심 값 - 데이터의 x_data의 값)**2 + (Class_B의 y를 뜻하는 인덱스 [1][0]에 해당하는 중심 값 - 데이터의 y_data의 값)**2
        # B중심 값에 대한 여섯 번째 데이터의 좌표에 대한 유클리드 계산 :제곱근((7-9)^2+(7-9)^2)
        B_eucliedean_distance_moem[i] = eucliedean_distance
        # 각각의 데이터들의 유클리드 계산 결과 값을 B_eucliedean_distance_moem에 저장한다.
        if(A_eucliedean_distance_moem[i] < B_eucliedean_distance_moem[i]):
            #A 중심 값에 대한 유클리드 계산 결과와 B 중심 값에 대한 유클리드 계산 결과 중 A 중심 값에 대한 계산 결과가 더 작을 경우
            Class_A[0].append(data[0][i])
            Class_A[1].append(data[1][i])
            #클래스 A에 소속된 데이터로 분류
        else:#그렇지 않다면
            #B 중심 값에 대한 유클리드 계산 결과와 A 중심 값에 대한 유클리드 계산 결과 중 B 중심 값에 대한 계산 결과가 더 작을 경우
            Class_B[0].append(data[0][i])
            Class_B[1].append(data[1][i])
            #클래스 B에 소속된 데이터로 분류
    #중심값을 결정하고 나서 분류한 데이터를 그래프로 보여준다.
    plt.plot(Class_A[0],Class_A[1],color='#FF0000',marker='o',markersize='12',linestyle='',label='Class_A_data')
    #초기의 Class_A에 소속된 데이터를 보여주기 위해 만든 plot() 함수를 이용해 데이터를 그려주었다.
    #Class_A의 데이터들의 위치를 보여주고, 색은 빨간색, 마커는 원형을 뜻하는 'o' 마커 사이즈는 12으로 설정하고 해당 데이터들의 라벨 이름을 'Class_A_data'로 지어주었다. 
    plt.plot(Class_B[0],Class_B[1],color='#0000FF',marker='o',markersize='12',linestyle='',label='Class_B_data')
    #초기의 Class_B에 소속된 데이터를 보여주기 위해 만든 plot() 함수를 이용해 데이터를 그려주었다.
    #Class_A의 데이터들의 위치를 보여주고, 색은 파란색, 마커는 원형을 뜻하는 'o' 마커 사이즈는 12으로 설정하고 해당 데이터들의 라벨 이름을 'Class_B_data'로 지어주었다. 
    plt.plot(Class_A_Midian[0],Class_A_Midian[1],color='#FF0000',marker='^',markersize='24',linestyle='',label='Class_A_Midian_data')
    #Class_A의 중심 값을 보여주기 위해 만든 plot() 함수를 이용해 데이터를 그려주었다.
    #각각의 데이터들의 위치를 보여주고, 색은 빨간색, 마커는 삼각형을 뜻하는 '^' 마커 사이즈는 24으로 설정하고 해당 데이터들의 라벨 이름을 'Class_A_Midian_data'로 지어주었다. 
    plt.plot(Class_B_Midian[0],Class_B_Midian[1],color='#0000FF',marker='h',markersize='24',linestyle='',label='Class_B_Midian_data')
    #Class_B의 중심 값을 보여주기 위해 만든 plot() 함수를 이용해 데이터를 그려주었다.
    #각각의 데이터들의 위치를 보여주고, 색은 파란색, 마커는 육각형을 뜻하는 'h' 마커 사이즈는 24으로 설정하고 해당 데이터들의 라벨 이름을 'Class_B_Midian_data'로 지어주었다.
    plt.legend(fontsize = '20')
    #그래프의 라벨명을 출력하기 위해 쓰이는 legend() 함수
    plt.show()
    #그래프를 화면에 보여주는 show() 함수이다.

    Class_A_Midian[0][0] = sum(Class_A[0])/len(Class_A[0])
    #분류된 Class_A의 x값의 평균을 구해서 다시 x값의 중심값을 찾는다.
    Class_A_Midian[1][0] = sum(Class_A[1])/len(Class_A[1])
    #분류된 Class_A의 y값의 평균을 구해서 다시 y값의 중심값을 찾는다.
    Class_B_Midian[0][0] = sum(Class_B[0])/len(Class_B[0])
    #분류된 Class_B의 x값의 평균을 구해서 다시 x값의 중심값을 찾는다.
    Class_B_Midian[1][0] = sum(Class_B[1])/len(Class_B[1])
    #분류된 Class_B의 y값의 평균을 구해서 다시 y값의 중심값을 찾는다.
    
    if Class_A_Midian == prev_Class_A_Midian and Class_B_Midian == prev_Class_B_Midian:
        #만약 이전 중심값이랑 새롭게 만들어진 중심값이 같다면 실행을 중지한다.
        print("중심값이 이전 중심값과 동일한 값을 찾아 멈췄습니다.")
        break
    else:#그렇지 않다면
        prev_Class_A_Midian[0][0] = Class_A_Midian[0][0]
        #이전의 Class_A의 중심값의 x값을 새로운 중심값의 x값을 저장한다.
        prev_Class_A_Midian[1][0] = Class_A_Midian[1][0]
        #이전의 Class_A의 중심값의 y값을 새로운 중심값의 y값을 저장한다. 
        prev_Class_B_Midian[0][0] = Class_B_Midian[0][0]
        #이전의 Class_B의 중심값의 x값을 새로운 중심값의 x값을 저장한다.
        prev_Class_B_Midian[1][0] = Class_B_Midian[1][0]
        #이전의 Class_B의 중심값의 y값을 새로운 중심값의 y값을 저장한다.
