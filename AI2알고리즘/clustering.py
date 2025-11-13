import matplotlib.pyplot as plt 
import math 

data = [[10.,20.,30.,70.,80.,90.],[10.,20.,30.,70.,80.,90.]]

Class_A_Midian = [[0],[0]]  
Class_B_Midian = [[0],[0]]  

Class_A_Midian[0][0] = min(data[0])
Class_A_Midian[1][0] = min(data[1])

Class_B_Midian[0][0] = max(data[0])
Class_B_Midian[1][0] = max(data[1])

prev_Class_A_Midian = [[10.],[10.]]
prev_Class_B_Midian = [[90.],[90.]]

plt.plot(data[0],data[1],color='#000000',marker='o',markersize='11',linestyle='',label='data')
plt.legend(fontsize = '12')
plt.title("set data")  
plt.show()

plt.plot(data[0],data[1],color='#000000',marker='o',markersize='12',linestyle='',label='data')
plt.plot(Class_A_Midian[0],Class_A_Midian[1],color='#FF0000',marker='^',markersize='14',linestyle='',label='Class_A_Midian_data')
plt.plot(Class_B_Midian[0],Class_B_Midian[1],color='#0000FF',marker='h',markersize='14',linestyle='',label='Class_B_Midian_data')
plt.legend(fontsize = '12')
plt.title("Class_A_Midian, Class_B_Midian data") 
plt.show() 

for i in range(0,6,1):  
    A_euclidean_distance_set = [0,0,0,0,0,0]    
    B_euclidean_distance_set = [0,0,0,0,0,0]     
    Class_A = [[],[]]  
    Class_B = [[],[]]    
    
    for i in range(0,len(data[0]),1):  
        euclidean_distance = math.sqrt((Class_A_Midian[0][0]-data[0][i])**2+(Class_A_Midian[1][0]-data[1][i])**2)
        A_euclidean_distance_set[i] = euclidean_distance
        euclidean_distance = math.sqrt((Class_B_Midian[0][0]-data[0][i])**2+(Class_B_Midian[1][0]-data[1][i])**2)
        B_euclidean_distance_set[i] = euclidean_distance
        
        if(A_euclidean_distance_set[i] < B_euclidean_distance_set[i]):
            Class_A[0].append(data[0][i])
            Class_A[1].append(data[1][i])            
        else:     
            Class_B[0].append(data[0][i])
            Class_B[1].append(data[1][i])
   
    plt.plot(Class_A[0],Class_A[1],color='#FF0000',marker='o',markersize='12',linestyle='',label='Class_A_data')
    plt.plot(Class_B[0],Class_B[1],color='#0000FF',marker='o',markersize='12',linestyle='',label='Class_B_data')
    plt.plot(Class_A_Midian[0],Class_A_Midian[1],color='#FF0000',marker='^',markersize='13',linestyle='',label='Class_A_Midian_data')
    plt.plot(Class_B_Midian[0],Class_B_Midian[1],color='#0000FF',marker='h',markersize='13',linestyle='',label='Class_B_Midian_data')
    plt.legend(fontsize = '13')
    plt.show()
   
    Class_A_Midian[0][0] = sum(Class_A[0])/len(Class_A[0])   
    Class_A_Midian[1][0] = sum(Class_A[1])/len(Class_A[1])  
    Class_B_Midian[0][0] = sum(Class_B[0])/len(Class_B[0])    
    Class_B_Midian[1][0] = sum(Class_B[1])/len(Class_B[1])    
    
    if Class_A_Midian == prev_Class_A_Midian and Class_B_Midian == prev_Class_B_Midian:   
        print(" 군집화 종료 ")
        break
    else:
        prev_Class_A_Midian[0][0] = Class_A_Midian[0][0] 
        prev_Class_A_Midian[1][0] = Class_A_Midian[1][0]  
        prev_Class_B_Midian[0][0] = Class_B_Midian[0][0]   
        prev_Class_B_Midian[1][0] = Class_B_Midian[1][0]   
 
