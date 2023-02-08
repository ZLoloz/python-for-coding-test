from random import randint
import time

#모든 프로그래밍은 결국 데이터를 다루는 행위입니다. 자료형에 대한 이해는 프로그래밍의 첫걸음이라 할 수 있습니다.

# 정수형(Integer) 양/음/0
a = 15
print('양의 정수 Integer = ', a)
a = -7
print('양의 정수 Integer = ', a)
a = 0
print('0 Integer = ', a)
#--------------------------------------------
# 실수형
a = 157.23
print('양의 실수 Integer = ', a)
a = -1932.2
print('음의 실수 Integer = ', a)
a = 5.
print('소수부가 0일 때, 0을 생략 Integer = ', a)
a = -.421
print('정수부가 0일 때, 0을 생략 Integer = ', a)
#--------------------------------------------
# 지수표현방식
# python에서는 e, E를 이용한 지수 표현 방식 이용 가능. (i.g. 1e9 : 10^9)
# 임의의 큰 수를 표현키 위해 사용.
# 최단경로 알고리즘 - 도달불가 노드에 대해 최단거리를 무한(INF)로 설정하곤 함. 이때 가능한 경로 최댓값이 10억 미만이라면, 무한값으로서 1e9를 이용가능함.
a = 1e9
print('10억 = ', a)
a = 75.25e1
print('75.25e1 => 75.25 x 10 = ', a)
a = 3954e-3
print('3954e-3 => 3954 x 1/1000 = ', a)
# 실수형 -> 정수형 변환
a = int(1e9)
print('실수형 -> 정수형 변환 = ', a)
#--------------------------------------------
# 컴퓨터는 이진수체계이기에, 10진수에서 특정 수의 경우 미세한 오차가 발생할 수 밖에 없다.
a = 0.3 + 0.6
print(a)
print('a == 0.9 ? ', a == 0.9)
print('3째자리에서 반올림 -> ', round(a,2))

# python3에서의 나눠진 결과는 실수가 반환된다.(2는 정수)

# /  : 실수형으로 반환
a = 2/3
print('2/3 = ', a)
# %  : 나머지 연산
a = 5%2
print('5%2 = ', a)
# // : 몫 연산
a = 5//3
print('5//3 = ', a)
# ** : 거듭제곱 연산
a = 2**3
print('2^3 = ', a)
#--------------------------------------------
# 리스트 자료형
# 연속적으로 담아 처리하기 위한 자료형
# Java의 Array의 기능 및 LinkedList와 유사한 기능 지원 / C++의 STL vector와 기능적으로 유사.
# 리스트 대신 배열 , 테이블이라 불리기도 함.
# 인덱스는 0부터 시작.
# [0,1]

# 크기가 n인, n개만큼 0이 담긴 리스트 초기화
n = 10 
a = [0] * n
print(a)

a = [1,2,3,4,5,6,7,8,9,0]
print('리스트 = ', a)
# 3번째 값
print('3번째 값 = ', a[2])
# 뒤에서 2번째 값 인덱싱
print('뒤에서 2번째 값 인덱싱 = ',a[-2])
# 슬라이싱 [a:b] => a <= index < b
print('[슬라이싱] 2~4번째 값 = ', a[1:4])
# 슬라이싱
print('[슬라이싱] 2~4번째 값 = ', a[1:-6])
# 리스트 초기화 방법의 하나 - List Comprehension(여러줄이 필요한 리스트초기화를 한줄로 작성되는 점이 장점.)
# 특히 2차원 리스트를 초기화 할 때 효과적으로 사용 가능.
a = [i for i in range(1, 10)]
print('1~9까지의 수를 포함하는 리스트 = ',a)
a = [ i for i in range(20) if i % 2 == 1]
print('0~19까지의 수 중에 홀수만 포함하는 리스트 = ', a)

# 2차원 리스트를 초기화 2x3
n = 2
m = 3
a = [[0] * m for _ in range(n)]
print(a) # [[0, 0, 0], [0, 0, 0]]
# 내부적으로 i가 사용되지 않을 때(반복되는 변수를 무시하고자 할때 언더바 사용됨.)
# append(value) | O(1)
# sort(reverse=false,true)   | O(NlogN)
# reverse()  | O(N) 
# insert(index, value)  | O(N)
# count(value)  | O(N)
# remove(value) | O(N)
# removeAll은 없음. -> List Comprehension 사용

a = [i for i in range(1, 10)]
remove_set = [3,5]
a = [i for i in a if i not in remove_set] # 
print('remove_set에 포함안된 값 \"목록\" = ', a)

#--------------------------------------------

#문자열 연산
a = "main"
b = "Submarine"
print(a + b)
print(a*3)
print(a + ' ' + b)
print(a[2:5])
print(a[2:5])
# 문자열은 특정 인덱스 값을 변경할 수는 없다.(Immutable)
# a[2] = 's' # 

#--------------------------------------------
# 튜플 자료형( ~ 1:11:10)
# 소괄호 이용. 한번 선언된 값은 변경 불가 const. 리스트에 비해 공간효율적.
a = (1,2,3,4,5,6,7,8,9) # (i for i in range(1, 10)) : generator
# a[1] = 3
print(a)
# 튜플 사용하면 좋은 경우
# 1) 서로 다른 성질의 데이터를 묶어 관리할 때 (itemId, price)
# 최단경로 알고리즘 (비용 , 노드번호)
# 데이터나열을 Hashing의 key값으로 사용해야 할 때 - 변경불가의 성질이 있어 key값으로서 사용될 수 있음.
# 3) 리스트보다 메모리르 효율적으로 사용해야 할 때
#--------------------------------------------
# 사전(dictionary) 자료형
# key,value

#--------------------------------------------

#--------------------------------------------

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1부터 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

end_time = time.time() # 측정 종료
print("선택 정렬 성능 측정:", end_time - start_time) # 수행 시간 출력

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1부터 100 사이의 랜덤한 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time) # 수행 시간 출력
