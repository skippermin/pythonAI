import matplotlib.pyplot as plt #matplotlib.pyplot 그래프 함수 
import math #수학 함수를 이용하기 위한 라이브러리

#K-means 알고리즘
#K = 클러스터의 개수(나누는 갯수)
#이차원 평면에서 (1,1)  (2,2)  (3,3)  (7,7)  (8,8)  (9,9)를 가지고 두 개의 군집화 
#중심값 두 개는 임의로 선정하고, 군집화가 되면 그래프로 군집에 따라 점들을 다른 색으로 표현
#처음엔 모두 검정색
#군집화가 되면 하나의 군집은 빨간색  다른 하나의 군집은 파란색

data = [[10.,20.,30.,70.,80.,90.],[10.,20.,30.,70.,80.,90.]]
#1번째 행에는 x_data의 값, 2번째 행에는 y_data의 값

Class_A_Midian = [[0],[0]]   # A클래스의 중심값을 선언과 동시에 (0, 0)으로 초기화
Class_B_Midian = [[0],[0]]   # B클래스의 중심값을 선언과 동시에 (0, 0)으로 초기화 

Class_A_Midian[0][0] = min(data[0])
Class_A_Midian[1][0] = min(data[1])
#A의 중심값은 (10, 10)으로 임의로 저장   #data에서 제일 작은 값을 저장
Class_B_Midian[0][0] = max(data[0])
Class_B_Midian[1][0] = max(data[1])
#B의 중심값은 (90, 90)으로 임의로 저장 #data에서 가장 큰 값을 저장 

prev_Class_A_Midian = [[10.],[10.]]
#A 중심값과 비교하기 위해 만들어진 이전의 중심값, (10, 10)으로 초기화
prev_Class_B_Midian = [[90.],[90.]]
#B 중심값과 비교하기 위해 만들어진 이전의 중심값,  (90, 90)으로 초기화

plt.plot(data[0],data[1],color='#000000',marker='o',markersize='11',linestyle='',label='data')
#초기의 데이터들을 나타냄 
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
#각각의 데이터들의 위치를 보여주고, 색은 검정색, 마커는 동그란원을 뜻하는 'o' 마커
#마커 사이즈는 11으로 설정하고 해당 데이터들의 라벨 이름을 'data'로 설정 
plt.legend(fontsize = '12')#그래프의 라벨명을 출력하기 위해 쓰이는 legend() 함수, 라벨 크기를 '12'으로 설정
plt.title("set data")  #그래프의 타이틀 명을 보여주는 함수
plt.show()  #그래프를 화면에 보여주는 함수

plt.plot(data[0],data[1],color='#000000',marker='o',markersize='12',linestyle='',label='data')
#초기의 데이터들을 나타냄 
#각각의 데이터들의 위치를 보여주고, 색은 검정색, 마커는 동그란원  'o' 마커 사이즈는 12으로 설정, 라벨 이름 'data' 
plt.plot(Class_A_Midian[0],Class_A_Midian[1],color='#FF0000',marker='^',markersize='14',linestyle='',label='Class_A_Midian_data')
#초기의 Class_A의 중심 값을 나타냄 
#데이터  위치를 보여주고, 색은 빨간색, 마커는 삼각형 '^' 마커 사이즈는 24으로 설정, 라벨 이름 'Class_A_Midian_data' 
plt.plot(Class_B_Midian[0],Class_B_Midian[1],color='#0000FF',marker='h',markersize='14',linestyle='',label='Class_B_Midian_data')
#초기의 Class_B의 중심 값을 나타냄 
#데이터 위치를 보여주고, 색은 파란색, 마커는 육각형 'h' 마커 사이즈는 24으로 설정,  라벨 이름 'Class_B_Midian_data'
plt.legend(fontsize = '12') #그래프의 라벨명을 출력 라벨 크기 '12'
plt.title("Class_A_Midian, Class_B_Midian data") #그래프의 타이틀 출력 
plt.show() #그래프를 화면에 출력 

for i in range(0,6,1):  #중심값과 데이터들의 거리 계산, 데이터들의 평균을 이용하여 새로운 중심값 계산 
    A_euclidean_distance_moem = [0,0,0,0,0,0]     #A 중심값에 대한 데이터들의 거리 초기화 
    B_euclidean_distance_moem = [0,0,0,0,0,0]      #B 중심값에 대한 데이터들의 거리 초기화
    Class_A = [[],[]]     #Class_A에 속하는 데이터를 저장 위한 리스트
    Class_B = [[],[]]      #Class_B에 속하는 데이터를 저장 위해 리스트 
    
    for i in range(0,len(data[0]),1):  # 중심값과 데이터의 거리를 계산하고, 중심값과 가까운 거리의 데이터를 저장
                                                        # 데이터를 0(초기값)으로 시작해 6(조건)보다 작을 때까지 1(증감식) 늘려주는 for문 생성
        euclidean_distance = math.sqrt((Class_A_Midian[0][0]-data[0][i])**2+(Class_A_Midian[1][0]-data[1][i])**2)
        # math.sqrt() 함수를 사용해 제곱근을 표현
        A_euclidean_distance_moem[i] = euclidean_distance
        # 각각의 데이터들의 유클리드 계산 결과를 A_eucliedean_distance_moem[i]에 저장
        euclidean_distance = math.sqrt((Class_B_Midian[0][0]-data[0][i])**2+(Class_B_Midian[1][0]-data[1][i])**2)
        # math.sqrt() 함수를 사용해 제곱근을 표현
        B_euclidean_distance_moem[i] = euclidean_distance
        # 각각의 데이터들의 유클리드 계산 결과를 B_eucliedean_distance_moem[i]에 저장
        
        if(A_euclidean_distance_moem[i] < B_euclidean_distance_moem[i]):
            #A 중심값에 대한 거리와 B 중심값에 대한 거리에서 A 중심값에 가까운 데이터 
            Class_A[0].append(data[0][i])
            Class_A[1].append(data[1][i])
            
        else:
             #A 중심값에 대한 거리와 B 중심값에 대한 거리에서 B 중심값에 가까운 데이터 
            Class_B[0].append(data[0][i])
            Class_B[1].append(data[1][i])
   
    #중심값을 결정한 후, 분류한 데이터 출력 
    plt.plot(Class_A[0],Class_A[1],color='#FF0000',marker='o',markersize='12',linestyle='',label='Class_A_data')
   
    plt.plot(Class_B[0],Class_B[1],color='#0000FF',marker='o',markersize='12',linestyle='',label='Class_B_data')

    plt.plot(Class_A_Midian[0],Class_A_Midian[1],color='#FF0000',marker='^',markersize='13',linestyle='',label='Class_A_Midian_data')
   
    plt.plot(Class_B_Midian[0],Class_B_Midian[1],color='#0000FF',marker='h',markersize='13',linestyle='',label='Class_B_Midian_data')

    plt.legend(fontsize = '13')   
    plt.show()
   
    Class_A_Midian[0][0] = sum(Class_A[0])/len(Class_A[0])   #분류된 Class_A의 x 평균을 이용하여 다시  x값의 중심값 생성
    Class_A_Midian[1][0] = sum(Class_A[1])/len(Class_A[1])   #분류된 Class_A의 y 평균을 이용하여  다시 y값의 중심값 생성 
    Class_B_Midian[0][0] = sum(Class_B[0])/len(Class_B[0])    #분류된 Class_B의 x 평균을 이용하여 다시  x값의 중심값 생성
    Class_B_Midian[1][0] = sum(Class_B[1])/len(Class_B[1])    #분류된 Class_B의 y 평균을 이용하여  다시 y값의 중심값 생성
    
    if Class_A_Midian == prev_Class_A_Midian and Class_B_Midian == prev_Class_B_Midian:   #이전 중심값과 새로운 중심값이 동일 
        print(" 군집화 종료 ")
        break
    else:
        prev_Class_A_Midian[0][0] = Class_A_Midian[0][0]   #이전 중심값 x에  새로운 중심값 x 저장
        prev_Class_A_Midian[1][0] = Class_A_Midian[1][0]   #이전 중심값 y에  새로운 중심값 y 저장 
        prev_Class_B_Midian[0][0] = Class_B_Midian[0][0]    #이전 중심값 x에  새로운 중심값 x 저장
        prev_Class_B_Midian[1][0] = Class_B_Midian[1][0]    #이전 중심값 y에  새로운 중심값 y 저장 
 
