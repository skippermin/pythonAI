from random import *  # 파이썬의 기본 랜덤 함수를 제공하는 random 모듈의 모든 구성을 코드에서 사용하기 위해 불러온다.
#  import 함수는 지정한 모듈에 속한 함수를 사용하기 위한 명령어이다.
#  import *에서 *는 모듈에 속한 모든 구성을 의미한다.
#  from은 import에서 사용할 모듈을 미리 지정하여, 모듈 이름을 지정하지 않고 바로 모듈의 함수를 사용할 수 있도록 해주는 명령어이다.
#  from random import *는 random 모듈에 속한 모든 구성을 모듈 이름 지정 없이 바로 사용할 수 있도록 해주겠다는 의미이다.
#  random 모듈은 실수, 정수 등의 랜덤한 값을 가지는 난수를 만드는 함수가 포함된 모듈이다. 

def decode(x):  #  2진수 4비트의 염색체를 10진수로 변환하는 사용자 정의 함수 decode를 만들고, 매개변수로 x를 사용한다.
#  파이썬에서 사용자 정의 함수를 만들기 위해 def 명령어를 사용한다.
#  파이썬에서 사용자 정의 함수의 매개변수는 별도의 타입을 지정하지 않으며, 매개변수에 정수나 실수, 문자열만이 아니라 리스트, 배열 등의 데이터도 받을 수 있다. 
# :은 블록을 의미하며, : 이후 여백(Tab키)으로 들여쓴 부분까지 함수의 실행 범위가 된다.

    tens = 0  #  decode 함수의 실행 결과 10진수를 저장할 변수 tens를 만들고 0을 대입해 초기화한다.

    for i in range(4):  #  for i in range(4): 를 사용하여 i 값이 0에서부터 3까지 4번 반복하는 for 반복문을 작성한다.
#  for i in range(4):는 i의 값이 0부터 4보다 작은 3의 값까지 반복하는 반복문이다.
#  파이썬에서 for 반복문은 매개변수에 List 혹은 Tuple 등의 여러 데이터로 이루어진 데이터를 순서대로 대입해 마지막까지 대입한 후 실행을 종료하는 반복문이다.
#  range 함수는 파이썬에서 정수형 리스트를 만드는 함수로, range 함수는 매개변수로 리스트의 시작 값, 리스트의 끝 미만 값, 리스트의 증감값을 받는다.
#  range(4)은 [0, 1, 2, 3] 리스트와 같다.
#  range(4)에서 시작값은 0, 끝값은 4 미만인 3, 증감값은 1이 된다.
#  range 함수의 매개변수에서 증감값은 실수를 사용할 수 없다.
#  range 함수의 매개변수에서 증감값은 생략할 수 있다. 증감값을 생략할 경우, 기본값은 1이 된다.
#  range 함수의 매개변수에서 증감값을 생략한 경우 시작값도 생략할 수 있다. 시작값을 생략할 경우, 기본값은 0이 된다.
#  range(4)는 range(0, 4, 1)과 같으며, range(0, 4)와 실행 결과가 같다.
# :은 블록을 의미하며, : 이후 여백(Tab키)으로 들여쓴 부분까지 for문의 반복 실행 범위가 된다.
#  함수 안에 for문을 사용하는 경우와 같이 여러 블록이 있을 경우, 블록의 개수에 맞춰 여백을 여러 번 사용해야 한다.

        if x[i] == '1':  #  x 리스트의 i번째 인덱스에 저장된 문자가 '1'과 같을 때 실행되는 if문을 작성한다. 
#  if문은 if 다음의 값이 true거나 0일 아닐 때 실행되는 조건문이다.
#  %은 두 값을 나눈 값의 나머지를 구하는 연산자이다.
#  ==은 비교연산자로 왼쪽 값과 오른쪽 값이 같으면 true, 왼쪽 값과 오른쪽 값이 다르면 false가 구해진다.
# :은 블록을 의미하며, : 이후 여백으로 들여쓴 부분까지 if문의 실행 범위가 된다.
#  x[i] == '1'이 true가 될 때는 '1' == '1'로 x[i]에 '1'이 저장되어 있을 때 if문이 실행된다.

            tens = tens + (2 ** (3 - i))  #  tens의 값에 2의 (3 – i) 제곱 값을 더한 값을 tens에 더하여 누적하는 것으로 2진수를 10진수로 변환한다.
#  ** 연산자는 파이썬에서 제곱 연산을 위해 사용한다. 2 ** (3 – i)은 2^(3 – i)를 의미한다.
#  2진수를 큰 값부터 불러오기 때문에, 제곱 연산에서 자릿수를 역으로 계산하기 위해 (3 – i)를 사용한다.
#  i의 값은 0부터 3이 되기 때문에, 2 ** (3 – i)은 순서대로 8, 4, 2, 1이 된다.

    return tens  # 2진수 문자열을 10진수로 변환한 tens의 값을 return을 사용하여 decode 함수의 종료와 함께 반환한다. 
#  return은 함수의 실행을 마치는 명령어이다.
#  return 다음에 변수나 값, 리스트나 배열 등을 사용해 함수의 실행 결과로 값을 함수를 호출한 지점으로 반환할 수 있다.

def fitness(x):  # 적합도 함수를 정의할 사용자 정의 함수 fitness를 만들고 매개변수로 x를 사용한다. 

    return (x * 15) - (x ** 2)  #  함수의 실행 결과로 적합도 함수인 (x * 15) - (x ** 2)를 반환한다.
#  (x * 15) - (x ** 2)는 15x – x^2 수식과 같다.

X = []  #  염색체를 4비트(4자리) 2진수 형태의 문자열로 저장하기 위한 리스트 X를 만들고 빈 리스트 []를 대입해 초기화한다.
#  []는 파이썬에서 List를 의미하며, List는 [] 대괄호를 사용한다.
#  List 안의 데이터의 구분은 , 쉼표로 구분한다.
#  List는 숫자, 문자열 등의 데이터를 지정하지 않고 자유롭게 사용할 수 있다.
#  파이썬에서는 []를 사용해 리스트를 빈 데이터로 초기화할 수 있다.

decodeX = []  #  2진수 염색체를 10진수로 변환한 디코딩 정수 값을 저장할 리스트 decodeX를 만들고 빈 리스트 []를 대입해 초기화한다.

fitX = []  #  염색체를 디코딩한 값으로 적합도를 구한 정수 값을 저장할 리스트 fitX를 만들고 빈 리스트 []를 대입해 초기화한다.

fitperX = []  # 각 세대 염색체들의 적합도의 합을 사용하여 적합도의 평균을 정수 값으로 저장할 리스트 fitperX를 만들고 빈 리스트 []를 대입해 초기화한다.

fitperDescX = []  #  fitperX를 내림차순 출력하기 위해 fitperX 리스트의 내림차순된 값을 저장할 리스트 fitperDescX를 만들고 빈 리스트 []를 대입해 초기화한다.

descindex = []  #  fitperX를 내림차순 출력하기 위해 fitperX 리스트의 내림차순된 값의 인덱스를 저장할 리스트 descindex를 만들고 빈 리스트 []를 대입해 초기화한다.

gene = 1  # 현재 염색체의 세대를 저장할 변수 gene를 만들고 정수 1을 대입한다. 

fit_set = 10  # 유전 알고리즘의 최대 세대(실행 횟수)를 저장할 변수 fit_set을 만들고 정수 10을 대입한다.

cross = 0.7  # 유전자의 교차율을 저장할 변수 cross를 만들고 실수 0.7(70%)을 대입한다.

mutat = 0.001  # 유전자의 변이율을 저장할 변수 mutat을 만들고 실수 0.001(0.1%)를 대입한다.

for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.
    lineStr = []  #  리스트 X를 2차원 리스트로 만들기 위해 사용할 리스트 lineStr을 만들고 빈 리스트 []를 대입해 초기화한다.

    linedecode = []  #  리스트 decodeX를 2차원 리스트로 만들기 위해 사용할 리스트 linedecode를 만들고 빈 리스트 []를 대입해 초기화한다.

    linefit = []  #  리스트 fitX를 2차원 리스트로 만들기 위해 사용할 리스트 linefit를 만들고 빈 리스트 []를 대입해 초기화한다.

    linefitper = []  #  X리스트를 2차원 리스트로 만들기 위해 사용할 리스트 linefitper를 만들고 빈 리스트 []를 대입해 초기화한다.

    fitperDescX.append(0)  #  파이썬의 리스트에 포함된 append 함수를 사용해 fitperDescX 리스트 데이터의끝에 append 함수의 매개변수로 사용된 정수 0을 추가한다. 
#  append 함수는 리스트의 마지막 인덱스 뒤에 매개변수로 사용된 데이터를 추가하는 리스트의 함수이다.

    descindex.append(0)  #  파이썬의 리스트에 포함된 append 함수를 사용해 descindex 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 정수 0을 추가한다. 

    for j in range(fit_set):  #  for j in range(fit_set): 을 사용하여 j 값이 0에서부터 fit_set 미만의 값까지 fit_set의 값만큼 반복하는 for 반복문을 작성한다.

        lineStr.append('')  #  파이썬의 리스트에 포함된 append 함수를 사용해 lineStr 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 빈 문자열 ''을 추가한다. 

        linedecode.append(0)  #  파이썬의 리스트에 포함된 append 함수를 사용해 linedecode 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 정수 0을 추가한다. 

        linefit.append(0)  #  파이썬의 리스트에 포함된 append 함수를 사용해 linefit 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 정수 0을 추가한다. 

        linefitper.append(0)  #  파이썬의 리스트에 포함된 append 함수를 사용해 linefitper 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 정수 0을 추가한다. 

    X.append(lineStr)  #  파이썬의 리스트에 포함된 append 함수를 사용해 X 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 리스트 lineStr을 추가하여, fit_set 길이의 리스트를 6개 가지는 2차원 리스트로 만든다. 

    decodeX.append(linedecode)  #  파이썬의 리스트에 포함된 append 함수를 사용해 decodeX 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 리스트 linedecode를 추가하여, fit_set 길이의 리스트를 6개 가지는 2차원 리스트로 만든다. 
#  append 함수로 리스트를 추가할 때, 같은 리스트를 매개변수로 사용해 여러 리스트에 추가하면 같은 메모리 주소를 참조하게 된다. 리스트가 같은 메모리 주소를 참조하게 되면, 한 리스트에서 값이 변경됐을 때 다른 리스트도 같은 메모리 주소를 참조해 값이 변하게 될 수 있다.
#  이 예제에서는 각각의 2차원 리스트가 독립된 값을 저장할 수 있도록, 2차원 리스트를 만들기 위해 append 함수에 사용하는 리스트를 각각 따로 만들어 다른 메모리 주소를 참조하게 만들었다.

    fitX.append(linefit)  #  파이썬의 리스트에 포함된 append 함수를 사용해 fitX 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 리스트 linefit를 추가하여, fit_set 길이의 리스트를 6개 가지는 2차원 리스트로 만든다. 

    fitperX.append(linefitper)  #  파이썬의 리스트에 포함된 append 함수를 사용해 fitperX 리스트 데이터의 끝에 append 함수의 매개변수로 사용된 리스트 linefitper를 추가하여, fit_set 길이의 리스트를 6개 가지는 2차원 리스트로 만든다. 

X[0][0] = '1100'  # 1세대의 첫번째 염색체(X[0][0])에 문자열 '1100'을 대입해 초기 염색체를 설정해준다. 

X[1][0] = '0100'  # 1세대의 두번째 염색체(X[1][0])에 문자열 '0100'을 대입해 초기 염색체를 설정해준다.

X[2][0] = '0001'  # 1세대의 세번째 염색체(X[2][0])에 문자열 '0001'을 대입해 초기 염색체를 설정해준다. 

X[3][0] = '1110'  # 1세대의 네번째 염색체(X[3][0])에 문자열 '1110'을 대입해 초기 염색체를 설정해준다. 

X[4][0] = '0111'  # 1세대의 다섯번째 염색체(X[4][0])에 문자열 '0111'을 대입해 초기 염색체를 설정해준다.

X[5][0] = '1001'  # 1세대의 여섯번째 염색체(X[5][0])에 문자열 '1001'을 대입해 초기 염색체를 설정해준다. 

fitsum = 0  # 염색체 적합도의 합을 저장할 변수 fitsum을 만들고 정수 0을 대입해 초기화한다. 

for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

    decodeX[i][0] = decode(X[i][0])  # 2진수 염색체 문자열을 저장한 X 리스트의 1세대 i번째인 [i][0] 인덱스가 가리키는 문자열을 decode 사용자 정의 함수에 매개변수로 사용해, 10진수로 변환된 decode 함수의 반환값을 decodeX 리스트의 i번째 0번 인덱스 [i][0]에 대입한다.

    fitX[i][0] = fitness(decodeX[i][0])  # 10진수 염색체 디코딩 값을 저장한 decodeX 리스트의 1세대 i번째인 [i][0] 인덱스가 가리키는 정수를 fitness 사용자 정의 함수에 매개변수로 사용해, 적합도 함수로 구해진 fitness 함수의 반환값을 fitX 리스트의 i번째 0번 인덱스 [i][0]에 대입한다.

    fitsum = fitsum + fitX[i][0]  # fitX 리스트의 [i][0] 인덱스의 값과 fitsum을 더한 값을 fitsum에 대입해 적합도 함수의 총합을 구한다.

for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

    per = (fitX[i][0] * 100) / fitsum  # 1세대의 염색체 적합도의 값을 가지고 있는 fitX 리스트의 [i][0] 인덱스에 저장된 값에 100을 곱한 후, 염색체 적합도 값의 총합인 fitsum으로 나눈 적합도 비율을 변수 per에 대입한다.

    fitperX[i][0] = int(per)  #  fitX[i][0]의 적합도 비율을 저장하고 있는 per를 int 함수로 정수로 변환한 후, 정수로 변환한 적합도 비율 값을 fitperX 리스트의 [i][0] 인덱스에 대입한다.

    fitperDescX[i] = int(per)  #  fitX[i][0]의 적합도 비율을 저장하고 있는 per를 int 함수로 정수로 변환한 후, 정수로 변환한 적합도 비율 값을 내림차순 정렬에 사용할 fitperDescX 리스트의 [i] 인덱스에 대입한다.

    descindex[i] = i  # for 반복문에 사용하는 조건변수 i의 값을 적합도 비율의 내림차순 값에 대한 인덱스 순번을 저장할 descindex 리스트의 [i] 인덱스에 대입한다.

for i in range(0, 5):  #  for i in range(0, 5): 를 사용하여 i 값이 0에서부터 4까지 5번 반복하는 for 반복문을 작성한다.
#  내림차순 정렬을 위해 값이 큰지 작은지 비교할 경우, 왼쪽 비교는 마지막 값 이전 인덱스의 값까지만 비교해도 오름차순 정렬을 수행할 수 있다.

    for j in range((i + 1), 6):  #  for j in range((i + 1), 6): 을 사용하여 j 값이 (i + 1)에서부터 5까지 (5 – i)번 반복하는 for 반복문을 작성한다.
# for i 반복문이 한 바퀴 돌 때마다 비교 범위에서 제일 큰 값이 제일 왼쪽 인덱스 리스트에 저장되기 때문에, i이하의 값은 비교하지 않아도 된다.

        if fitperDescX[i] < fitperDescX[j]:  #  if문을 사용하여 리스트 fitperDescX의 i 인덱스에 저장된 값이 j 인덱스에 저장된 값보다 작으면 동작하는 if문을 작성한다.
#  <은 비교연산자로 왼쪽 값이 오른쪽 값보다 작으면 true, 왼쪽 값이 오른쪽 값보다 크거나 같으면 false가 구해진다.
# if fitperDescX[i] < fitperDescX[j]:가 실행될 때마다 fitperDescX 리스트의 큰 값은 fitperDescX[i]에 저장되고 리스트에서 작은 값은 fitperDescX[j]에 저장되어 내림차순 정렬이 수행된다.

            temp = fitperDescX[i]  # 내림차순 정렬을 위해 fitperDescX의 [i] 인덱스 위치에 저장된 값을 temp에 대입한다.

            fitperDescX[i] = fitperDescX[j]  # fitperDescX의 [j] 인덱스 위치에 저장된 값을 fitperDescX의 [i] 인덱스 위치에 대입한다.

            fitperDescX[j] = temp  # fitperDescX 리스트의 i 인덱스 위치에 저장된 값을 가지고 있는 temp를 fitperDescX 리스트의 j 인덱스 위치에 대입해 fitperDescX[i]와 fitperDescX[j] 값을 교환한다.
#  if문 안의 코드를 통하여 if문이 실행될 때마다 fitperDescX[i]와 fitperDescX[j] 값을 교환해 리스트의 왼쪽에 더 큰 값이 오도록 한다.

            temp = descindex[i]  # 내림차순 정렬 결과에 따른 인덱스 순서를 변경하기 위해 descindex의 [i] 인덱스 위치에 저장된 값을 temp에 대입한다.

            descindex[i] = descindex[j]  # descindex의 [j] 인덱스 위치에 저장된 값을 descindex의 [i] 인덱스 위치에 대입한다.

            descindex[j] = temp  # descindex 리스트의 i 인덱스 위치에 저장된 값을 가지고 있는 temp를 descindex 리스트의 j 인덱스 위치에 대입해 descindex[i]와 descindex[j] 값을 교환하고 내림차순 정렬된 결과에 따른 인덱스 순번을 descindex 리스트에 저장한다.

print(gene, "세대 염색체 적합도", sep = '')  # print 함수를 사용해 gene의 값과 문자열을 차례대로 출력한다. 
#  print 함수는 변수 혹은 문자열을 콘솔 화면에 출력하는 함수이다.
#  print 함수에서 여러 변수 혹은 문자열을 출력하기 위해, 변수 혹은 문자열을 ,(콤마)로 구분한다.
#  print 함수는 변수 혹은 문자열을 출력할 때 간격을 sep 옵션으로 설정한다. sep는 기본값으로 sep = ' '을 가지고 있다. 
#  이 예제에서는 출력할 때의 간격을 없애기 위해 sep = ''을 사용했다.

for i in descindex: #  for i in descindex: 를 사용하여 i 값이 적합도 비율을 내림차순했을 때의 인덱스를 저장한 리스트인 descindex에 저장된 값 순서대로 6번 반복하는 for 반복문을 작성한다.

    print("<X", (i + 1), gene, " ", X[i][0], " ", decodeX[i][0], " 적합도 ", fitX[i][0], " 적합도 비율 ", fitperX[i][0], ">", end = '  ', sep = '')  #  print 함수를 사용해 염색체 2진수, 10진수, 적합도, 적합도 비율을 순서대로 출력하며, 출력할 때의 변수 혹은 문자열 사이의 여백 sep는 빈 문자열 ''로 설정하고 print 함수로 출력이 끝났을 때 추가로 출력할 문자열 end는 두 칸 띄어쓰기인 '  '로 설정한다.
#  print 함수에서 end는 print 함수가 끝난 후 추가로 출력할 문자열을 의미한다. end의 기본값은 한 줄 띄어쓰는 \n이다.

print("\n\n")  #  print 함수를 사용해 "\n\n" 문자열을 출력해 줄넘김을 수행한다.
# "\n\n" 문자열에서 \n은 이스케이프 시퀀스로, 이스케이프 시퀀스는 프로그래밍 언어 특성상 표현할 수 없는 문자 혹은 기능을 사용하기 위한 특수한 문자 집합이다.
#  \n은 한 줄 줄넘김을 의미한다.

sum_per = 0.0  # 적합도 비율의 합을 저장할 변수 sum_per을 만들고 0.0을 대입해 초기화한다.

index_1 = 0  # 교차 혹은 변이가 일어날 때 염색체 순번을 지정할 첫번째 인덱스 변수 index_1을 만들고 0을 대입해 초기화한다.

index_2 = 0  # 교차가 일어날 때 염색체 순번을 지정할 두번째 인덱스 변수 index_2를 만들고 0을 대입해 초기화한다.

while fit_set != gene:  #  while fit_set != gene:를 사용하여 fit_set의 값과 gene의 값이 일치할 때까지 반복하는 while 반복문을 작성한다.
#  파이썬에서 while 반복문은 while 반복문에 사용한 조건식이 false가 될 때까지 반복 실행되는 반복문이다.
#  !=은 비교연산자로 왼쪽의 값과 오른쪽 값이 다를 때 true, 왼쪽의 값과 오른쪽 값이 같을 때 false가 구해진다.
#  while문은 반복문 실행 범위 안에 조건식에 사용한 변수의 값을 변하게 하는 코드가 있어야 한다.
#  while문의 실행 범위 안에서 조건식의 변수 값이 변하지 않는다면, while문이 항상 true여서 무한 루프가 발생할 수 있다.
# :은 블록을 의미하며, : 이후 여백으로 들여쓴 부분까지 while문의 반복 실행 범위가 된다.

    count = 0  # 다음 세대의 유전자 개수를 체크할 변수 count를 만들고 0을 대입한다.

    while count != 6: #  while count != 6을 사용하여 count의 값이 6으로 일치하고 다음 세대의 6개 염색체를 만들 때까지 반복하는 while 반복문을 작성한다.

        rand = uniform(0.0, cross + mutat)  # random 모듈에서 정해진 범위 내의 실수형 난수를 만드는 uniform 함수를 사용해, 0.0부터 교차율 cross에 변이율 mutat을 더한 값 이하까지의 실수형 난수를 만들어 rand에 대입해 저장한다.
#  uniform 함수는 파이썬 기본 모듈인 random에 포함된 모듈로, 매개변수로 실수형 난수를 만들 때의 최소값과 최대값을 받는다. 
#  uniform 함수로 만들어지는 실수는, 매개변수로 사용된 최소값과 최대값 둘 다 포함된 범위 내의 난수를 만든다.

        if rand > mutat:  #  if문을 사용하여 변수 rand에 저장된 난수가 변이율 mutat보다 커, 교차율이 범위의 난수일 때 동작하는 if문을 작성한다.
#  >은 비교연산자로 왼쪽 값이 오른쪽 값보다 크면 true, 왼쪽 값이 오른쪽 값보다 작거나 같으면 false가 구해진다.

            index_1 = 0  # 염색체 교차가 발생할 때의 첫번째 염색체를 지정할 index_1의 값을 0으로 초기화한다.

            index_2 = 0  # 염색체 교차가 발생할 때의 두번째 염색체를 지정할 index_2의 값을 0으로 초기화한다.

            sum_per = 0.0  # 적합도 비율의 합을 저장할 변수 sum_per에 0.0을 대입해 초기화한다.

            while index_1 == index_2:  #  while index_1 == index_2:를 사용하여 index_1의 값과 index_2의 값이 일치하지 않을 때까지 반복하는 while 반복문을 작성한다.
#  ==은 비교 연산자로 왼쪽 값과 오른쪽 값이 같으면 true, 왼쪽 값과 오른쪽 값이 다르면 false가 구해진다.

                for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                    sum_per = sum_per + fitperX[i][(gene - 1)]  # sum_per 변수에 적합도 비율 fitperX 리스트의 [i][(gene - 1)] 인덱스에 저장된 값을 더한 값을 sum_per에 대입해, 현재 세대의 모든 적합도 비율의 합을 sum_per에 누적시킨다.

                rand_1 = uniform(0.0, sum_per)  # random 모듈에서 정해진 범위 내의 실수형 난수를 만드는 uniform 함수를 사용해, 0.0부터 교차율 cross에 모든 적합도 비율의 합 sum_per 이하까지의 실수형 난수를 만들어 rand_1에 대입해 저장한다.

                rand_2 = uniform(0.0, sum_per)  # random 모듈에서 정해진 범위 내의 실수형 난수를 만드는 uniform 함수를 사용해, 0.0부터 교차율 cross에 모든 적합도 비율의 합 sum_per 이하까지의 실수형 난수를 만들어 rand_2에 대입해 저장한다.

                sum_per = 0.0  # 적합도 비율의 합을 저장할 변수 sum_per에 0.0을 대입해 초기화한다.

                for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                    sum_per = sum_per + fitperX[i][(gene - 1)]  # sum_per 변수에 적합도 비율 fitperX 리스트의 [i][(gene - 1)] 인덱스에 저장된 값을 더한 값을 sum_per에 대입해, 현재 세대의 적합도 비율의 합을 sum_per에 누적시키며 rand_1이 몇 번째 적합도 비율에 포함되어 있는지 검색한다.

                    if rand_1 <= sum_per:  #  if문을 사용하여 변수 rand_1에 저장된 난수가 현재 적합도 비율의 누적 값을 저장한 값 sum_per보다 작거나 같아, 현재 [i]번째 적합도 비율에 rand_1이 포함될 때 실행되는 if문을 작성한다.
#  <=은 비교연산자로 왼쪽 값이 오른쪽 값보다 작거나 같으면 true, 왼쪽 값이 오른쪽 값보다 크면 false가 구해진다.

                        index_1 = i  # 염색체 교차가 발생할 때의 첫번째 염색체를 지정할 index_1에 i 값을 대입한다.

                        break  # break 명령문을 사용해 for i in range(6): 반복문을 강제로 종료하고, 다음 코드를 실행한다.
#  break 명령문은 break문을 호출한 for, while 등의 구문에서 탈출하고, break를 호출한 for 구문이 끝나는 다음 코드를 실행한다.

                sum_per = 0.0  # 적합도 비율의 합을 저장할 변수 sum_per에 0.0을 대입해 초기화한다.

                for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                    sum_per = sum_per + fitperX[i][(gene - 1)]  # sum_per 변수에 적합도 비율 fitperX 리스트의 [i][(gene - 1)] 인덱스에 저장된 값을 더한 값을 sum_per에 대입해, 현재 세대의 적합도 비율의 합을 sum_per에 누적시키며 rand_2이 몇 번째 적합도 비율에 포함되어 있는지 검색한다.

                    if rand_2 <= sum_per: #  if문을 사용하여 변수 rand_2에 저장된 난수가 현재 적합도 비율의 누적 값을 저장한 값 sum_per보다 작거나 같아, 현재 [i]번째 적합도 비율에 rand_2이 포함될 때 실행되는 if문을 작성한다.

                        index_2 = i  # 염색체 교차가 발생할 때의 두번째 염색체를 지정할 index_2에 i 값을 대입한다.

                        break  # break 명령문을 사용해 for i in range(6): 반복문을 강제로 종료하고, 다음 코드를 실행한다.

            crossX_1 = list(X[index_1][(gene - 1)])  # X 염색체의 현재 세대의 index_1번째 염색체를 가리키는 [index_1][(gene - 1)] 인덱스에 저장된 2진수 염색체 문자열을 각 문자별로 리스트로 나눠, 나누어진 문자 리스트를 crossX_1에 대입한다.
#  list 함수는 파이썬 기본 함수로, 리스트에 저장된 요소를 각각 분해하여 새로운 리스트를 만들어내는 함수이다.

            crossX_2 = list(X[index_2][(gene - 1)]) # X 염색체의 현재 세대의 index_2번째 염색체를 가리키는 [index_2][(gene - 1)] 인덱스에 저장된 2진수 염색체 문자열을 각 문자별로 리스트로 나눠, 나누어진 문자 리스트를 crossX_2에 대입한다.

            cross_min = len(crossX_1) - round(len(crossX_1) * cross)  # crossX_1 리스트의 길이에 crossX_1 리스트에 교차율 cross를 곱한 값의 반올림 값을 뺀, 교차할 염색체 인덱스의 최소값을 cross_min에 대입한다.
#  len은 파이썬 기본 제공 함수로, 매개변수로 사용된 리스트의 길이(요소 개수)를 정수로 반환한다.
#  round는 파이썬 기본 제공 함수로, 매개변수로 사용된 실수를 반올림하는 함수이다. 
#  round 함수는 매개변수로 반올림할 값과 반올림할 소수점 자릿수를 받는다.
#  round 함수의 매개변수 중 소수점 자릿수를 생략하면, 소수점 첫째 자릿수를 반올림해 정수를 만든다.

            cross_max = len(crossX_1)  # crossX_1 리스트의 길이를 구해, 교차할 염색체 인덱스의 최대값으로 cross_max에 대입한다.

            for i in range(cross_min, cross_max):  #  for i in range(cross_min, cross_max): 를 사용하여 i 값이 cross_min에서부터 cross_max 미만인 (cross_max – 1)까지 반복하는 for 반복문을 작성한다.

                temp = crossX_1[i]  # 염색체 교차를 위해 crossX_1의 [i] 인덱스 값을 temp에 대입한다.

                crossX_1[i] = crossX_2[i]  # crossX_2의 [i] 인덱스 위치에 저장된 값을 crossX_1의 [i] 인덱스 위치에 대입한다.

                crossX_2[i] = temp  # crossX_1 리스트의 [i] 인덱스 위치에 저장된 값을 가지고 있는 temp를 crossX_2 리스트의 [i] 인덱스 위치에 대입해 crossX_1[i]와 crossX_2[i] 값을 교차한다.

            for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                if X[i][gene] == "".join(crossX_1):  # 다음 세대를 저장할 X 리스트의 [i][gene] 인덱스에 저장된 2진수 염색체 문자열과 crossX_1 리스트를 join 함수를 사용해 하나의 문자열로 변환한 문자열이 같아, 다음 세대 염색체와 교차한 염색체가 같을 때 동작하는 if문을 작성한다.
#  .join은 파이썬 기본 제공 함수로써, 리스트의 요소들을 하나로 연결해주는 함수이다.
#  .join 함수는 리스트의 요소들을 연결할 때, 리스트의 요소들 사이에 특정 문자열을 삽입할 수 있다.
#  "".join은 리스트의 요소들을 연결할 때, 리스트의 요소들 사이에 빈 문자열 ""을 삽입한다는 의미이다. 

                    index_1 = -1  # crossX_1의 염색체와 같은 염색체가 이미 있다는 의미로, index_1에 -1을 대입한다.

                    break  # break 명령문을 사용해 for i in range(6): 반복문을 강제로 종료하고, 다음 코드를 실행한다.

            for i in range(6):   #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                if X[i][gene] == "".join(crossX_2):  # 다음 세대를 저장할 X 리스트의 [i][gene] 인덱스에 저장된 2진수 염색체 문자열과 crossX_2 리스트를 join 함수를 사용해 하나의 문자열로 변환한 문자열이 같아, 다음 세대 염색체와 교차한 염색체가 같을 때 동작하는 if문을 작성한다.

                    index_2 = -1 # crossX_2의 염색체와 같은 염색체가 이미 있다는 의미로, index_2에 -1을 대입한다.

                    break  # break 명령문을 사용해 for i in range(6): 반복문을 강제로 종료하고, 다음 코드를 실행한다.

            if (index_1 != -1) and (count != 6):  #  index_1이 -1이 아니고, 염색체의 개수를 저장하는 count가 6이 아닐 때 실행되는 if문을 작성한다.
#  and는 왼쪽과 오른쪽이 모두 true일 때 true, 왼쪽과 오른쪽이 모두 true가 아니라면 false가 구해진다.

                X[count][gene] = "".join(crossX_1)  # crossX_1 리스트를 join 함수를 사용해 하나의 문자열로 변환한 2진수 염색체 문자열을 X 리스트의 다음 세대의 count번째인 [count][gene] 인덱스에 대입한다. 

                count = count + 1  #  염색체의 개수를 저장하는 count에 1을 더한 값을 count에 대입해 누적한다.

            if (index_2 != -1) and (count != 6):  #  index_2가 -1이 아니고, 염색체의 개수를 저장하는 count가 6이 아닐 때 실행되는 if문을 작성한다.

                X[count][gene] = "".join(crossX_2)  # crossX_2 리스트를 join 함수를 사용해 하나의 문자열로 변환한 2진수 염색체 문자열을 X 리스트의 다음 세대의 count번째인 [count][gene] 인덱스에 대입한다. 

                count = count + 1 #  염색체의 개수를 저장하는 count에 1을 더한 값을 count에 대입해 누적한다.

        else:  #  변수 rand에 저장된 난수가 변이율 mutat보다 작거나 같아, if rand > mutat: 이 false일 때 동작하는 else문을 작성한다.
# else문은 if문의 조건이 모두 false일 때 실행되는 블록으로, else문은 생략할 수 있다.

            for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                sum_per = sum_per + fitperX[i][(gene - 1)] # sum_per 변수에 적합도 비율 fitperX 리스트의 [i][(gene - 1)] 인덱스에 저장된 값을 더한 값을 sum_per에 대입해, 현재 세대의 모든 적합도 비율의 합을 sum_per에 누적시킨다.

            rand_1 = uniform(0.0, sum_per)  # random 모듈에서 정해진 범위 내의 실수형 난수를 만드는 uniform 함수를 사용해, 0.0부터 교차율 cross에 모든 적합도 비율의 합 sum_per 이하까지의 실수형 난수를 만들어 rand_1에 대입해 저장한다.

            sum_per = 0.0  # 적합도 비율의 합을 저장할 변수 sum_per에 0.0을 대입해 초기화한다.

            for i in range(6): #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

                sum_per = sum_per + fitperX[i][(gene - 1)] # sum_per 변수에 적합도 비율 fitperX 리스트의 [i][(gene - 1)] 인덱스에 저장된 값을 더한 값을 sum_per에 대입해, 현재 세대의 모든 적합도 비율의 합을 sum_per에 누적시킨다.

                if rand_1 <= sum_per:  #  if문을 사용하여 변수 rand_1에 저장된 난수가 현재 적합도 비율의 누적 값을 저장한 값 sum_per보다 작거나 같아, 현재 [i]번째 적합도 비율에 rand_1이 포함될 때 실행되는 if문을 작성한다.
#  <=은 비교연산자로 왼쪽 값이 오른쪽 값보다 작거나 같으면 true, 왼쪽 값이 오른쪽 값보다 크면 false가 구해진다.

                    index_1 = i   # 염색체 교차가 발생할 때의 첫번째 염색체를 지정할 index_1에 i 값을 대입한다.

                    break  # break 명령문을 사용해 for i in range(6): 반복문을 강제로 종료하고, 다음 코드를 실행한다.

            crossX_1 = list(X[index_1][(gene - 1)])  # X 염색체의 현재 세대의 index_1번째 염색체를 가리키는 [index_1][(gene - 1)] 인덱스에 저장된 2진수 염색체 문자열을 각 문자별로 리스트로 나눠, 나누어진 문자 리스트를 crossX_1에 대입한다.

            temp = crossX_1[0]  # 염색체 변이를 위해 crossX_1의 [0] 인덱스 값을 temp에 대입한다.

            crossX_1[0] = crossX_1[1]  # crossX_1의 [1] 인덱스 위치에 저장된 값을 crossX_1의 [0] 인덱스 위치에 대입한다.

            crossX_1[1] = temp  # crossX_1 리스트의 [0] 인덱스 위치에 저장된 값을 가지고 있는 temp를 crossX_1 리스트의 [1] 인덱스 위치에 대입해 crossX_1[0]과 crossX_1[0] 값으로 변이한다.

            X[count][gene] = "".join(crossX_1)  # crossX_1 리스트를 join 함수를 사용해 하나의 문자열로 변환한 2진수 염색체 문자열을 X 리스트의 다음 세대의 count번째인 [count][gene] 인덱스에 대입한다. 

            count = count + 1  #  염색체의 개수를 저장하는 count에 1을 더한 값을 count에 대입해 누적한다.

    fitsum = 0  # 염색체 적합도의 합을 저장할 변수 fitsum에 정수 0을 대입한다. 

    for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

        decodeX[i][gene] = decode(X[i][gene])  # 2진수 염색체 문자열을 저장한 X 리스트의 (gene + 1)번째 세대 i번째인 [i][gene] 인덱스가 가리키는 문자열을 decode 사용자 정의 함수에 매개변수로 사용해, 10진수로 변환된 decode 함수의 반환값을 decodeX 리스트의 i번째 gene 세대 인덱스 [i][gene]에 대입한다.

        fitX[i][gene] = fitness(decodeX[i][gene])  # 10진수 염색체 디코딩 값을 저장한 decodeX 리스트의 (gene + 1)세대 i번째인 [i][gene] 인덱스가 가리키는 정수를 fitness 사용자 정의 함수에 매개변수로 사용해, 적합도 함수로 구해진 fitness 함수의 반환값을 fitX 리스트의 i번째 (gene + 1) 세대 인덱스 [i][gene]에 대입한다.

        fitsum = fitsum + fitX[i][gene]  # fitX 리스트의 [i][gene] 인덱스의 값과 fitsum을 더한 값을 fitsum에 대입해 적합도 함수의 총합을 구한다.

    for i in range(6):  #  for i in range(6): 를 사용하여 i 값이 0에서부터 5까지 6번 반복하는 for 반복문을 작성한다.

        per = (fitX[i][gene] * 100) / fitsum  # (gene + 1)세대의 염색체 적합도의 값을 가지고 있는 fitX 리스트의 [i][gene] 인덱스에 저장된 값에 100을 곱한 후, 염색체 적합도 값의 총합인 fitsum으로 나눈 적합도 비율을 변수 per에 대입한다.

        fitperX[i][gene] = int(per)  #  fitX[i][gene]의 적합도 비율을 저장하고 있는 per를 int 함수로 정수로 변환한 후, 정수로 변환한 적합도 비율 값을 fitperX 리스트의 [i][gene] 인덱스에 대입한다.

        fitperDescX[i] = int(per)  #  fitX[i][gene]의 적합도 비율을 저장하고 있는 per를 int 함수로 정수로 변환한 후, 정수로 변환한 적합도 비율 값을 내림차순 정렬에 사용할 fitperDescX 리스트의 [i] 인덱스에 대입한다.

        descindex[i] = i  # for 반복문에 사용하는 조건변수 i의 값을 적합도 비율의 내림차순 값에 대한 인덱스 순번을 저장할 descindex 리스트의 [i] 인덱스에 대입한다.

    for i in range(0, 5):  #  for i in range(0, 5): 를 사용하여 i 값이 0에서부터 4까지 5번 반복하는 for 반복문을 작성한다.

        for j in range((i + 1), 6):  #  for j in range((i + 1), 6): 을 사용하여 j 값이 (i + 1)에서부터 5까지 (5 – i)번 반복하는 for 반복문을 작성한다.

            if fitperDescX[i] < fitperDescX[j]:  #  if문을 사용하여 리스트 fitperDescX의 i 인덱스에 저장된 값이 j 인덱스에 저장된 값보다 작으면 동작하는 if문을 작성한다.

                temp = fitperDescX[i]  # 내림차순 정렬을 위해 fitperDescX의 [i] 인덱스 위치에 저장된 값을 temp에 대입한다.

                fitperDescX[i] = fitperDescX[j]  # fitperDescX의 [j] 인덱스 위치에 저장된 값을 fitperDescX의 [i] 인덱스 위치에 대입한다.

                fitperDescX[j] = temp  # fitperDescX 리스트의 i 인덱스 위치에 저장된 값을 가지고 있는 temp를 fitperDescX 리스트의 j 인덱스 위치에 대입해 fitperDescX[i]와 fitperDescX[j] 값을 교환한다.

                temp = descindex[i]  # 내림차순 정렬 결과에 따른 인덱스 순서를 변경하기 위해 descindex의 [i] 인덱스 위치에 저장된 값을 temp에 대입한다.

                descindex[i] = descindex[j]  # descindex의 [j] 인덱스 위치에 저장된 값을 descindex의 [i] 인덱스 위치에 대입한다.

                descindex[j] = temp  # descindex 리스트의 i 인덱스 위치에 저장된 값을 가지고 있는 temp를 descindex 리스트의 j 인덱스 위치에 대입해 descindex[i]와 descindex[j] 값을 교환하고 내림차순 정렬된 결과에 따른 인덱스 순번을 descindex 리스트에 저장한다.

    print((gene + 1), "세대 염색체 적합도", sep = '')  # print 함수를 사용해 gene의 값과 문자열을 차례대로 출력한다.

    for i in descindex:  #  for i in descindex: 를 사용하여 i 값이 적합도 비율을 내림차순했을 때의 인덱스를 저장한 리스트인 descindex에 저장된 값 순서대로 6번 반복하는 for 반복문을 작성한다.

        print("<X", (i + 1), (gene + 1), " ", X[i][gene], " ", decodeX[i][gene], " 적합도 " ,fitX[i][gene], " 적합도 비율 ", fitperX[i][gene], ">", end = '  ', sep = '')  #  print 함수를 사용해 염색체 2진수, 10진수, 적합도, 적합도 비율을 순서대로 출력하며, 출력할 때의 변수 혹은 문자열 사이의 여백 sep는 빈 문자열 ''로 설정하고 print 함수로 출력이 끝났을 때 추가로 출력할 문자열 end는 두 칸 띄어쓰기인 '  '로 설정한다.

    print("\n\n")  #  print 함수를 사용해 "\n\n" 문자열을 출력해 줄넘김을 수행한다.

    gene = gene + 1  #  현재 세대의 적합도와 적합도 비율까지 구한 후, 다음 세대로 넘어가기 위해 gene에 1을 더한 값을 gene에 대입해 gene의 값을 1씩 누적시킨다.
