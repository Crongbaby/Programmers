# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xjueCttO2RM7kJX7wsFUzb8pNDLBWr4z

**정렬 1번째 문제, K번째 수**

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3
"""

def solution(array, commands):
    ind=[]; new_arr=[]; k_list=[];
    for ele1 in commands:
        ind = [] #command 요소 리스트 다시 초기화
        for ele2 in ele1:
            ind.append(ele2) #첫번째 command 리스트 안에 리스트 요소 추가
        new_arr = array[ind[0]-1:ind[1]] #ind 리스트의 첫번째 두 번째 숫자까지 슬라이싱(인덱스는 0부터 시작, 인덱스-1)
        k_list.append(sorted(new_arr)[ind[2]-1]) #오름차순 정렬, ind 리스트의 2번재 값(k번째)에서 -1한 값을 k_리스트에 넣기기 (인덱스가 0부터 시작해서)
    return(k_list) #반환

#실험용
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#다른 사람 풀이
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer

#K번째 수 (영창님, 재현님님)
def solution(array, commands):
    answer = []

    for i in commands:
        cut = array[(i[0]-1) : i[1]]
        cut.sort()
        answer.append(cut[i[2]-1])

    return answer

"""**정렬 2번째 문제, 가장 큰 수**

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
"""

#1차 시도 실패
def solution(numbers):
    #sort의 key 문법 사용, 내림차순으로 정렬
    #str로 맨 앞자리의 숫자가 가장 큰 수부터 정렬, 같으면 그 후에 숫자 비교해서 큰 값으로
    #10보다 작은 수가 중간에 섞이면 안 되고 조건에 따라 다르게 들어가야함
    numbers_one = []
    numbers_one.extend(sorted([i for i in numbers if (i<10 and i!=0)],reverse=False)) #10 아래 숫자만 추출(0 제외, 0은 sort에서 알아서 맨 뒤로로)

    #리스트 빼기 리스트
    all_sub_one = [x for x in numbers if x not in numbers_one]
    
    #10 이상의 원소들끼리만 오름차순 정렬, lambda 사용? 2 3 22
    all_sub_one.sort(key=str, reverse = True) #10 이상의 원소들끼리만 오름차순 정렬 
    print(all_sub_one) #아니 여기부터 문제가 나면 우째

    # solution([3, 30, 34, 5, 9]) 330 > 303
    #직접 10 아래 숫자 넣어주기 
    for i in numbers_one:
      for j in range(len(all_sub_one)):
        if(all_sub_one[j] >= 100 and i!=0): #100 이상
          if(i > (all_sub_one[j]//100)): #100 이상의 맨 앞의 숫자보다 클 때
            all_sub_one.insert(j,i) #그 자리에 삽입
            break
          elif(i== (all_sub_one[j]//100)): #100 이상의 맨 앞의 숫자랑 같을 때
            if(i >= ((all_sub_one[j]%100)//10)): #100 이상에서 i가 십의 자리 보다 큰 경우
              all_sub_one.insert(j,i) #그 자리에 삽입
              break
            else: #100 이상에서 i가 십의 자리 보다 작을 경우
              all_sub_one.insert(j+1,i) #그 다음에 삽입(뒤에 가야 더 큰 수가 됨)
              break
        else: #100 미만 10 이상
          if(i > (all_sub_one[j]//10)): #맨 앞의 숫자와 비교
            all_sub_one.insert(j,i) 
            break
          elif(i == (all_sub_one[j]//10)): #맨 앞의 숫자와 비교
            if(i > (all_sub_one[j]%10)): #10 이상에서 i가 일의 자리 보다 큰 경우
              all_sub_one.insert(j,i) #그 자리에 삽입
              break
            else: #i가 일의 자리 보다 작을 경우
              all_sub_one.insert(j+1,i) #그 다음에 삽입(뒤에 가야 더 큰 수가 됨)
              break
    if sum(all_sub_one)==0: print('0')
    else:
      result = ''.join(str(s) for s in all_sub_one) #리스트 문자열로 변환
      print(result)
    
# solution([6, 10, 2])
# solution([3, 30, 34, 5, 9])
solution([232,23]) #오류 23232
solution([212,21])
solution([70,0,0,0,0])
solution([0,0,0,0])

#인터넷 뒤져서 람다식 써보기 (2차 시도)
#세 자리 수로 만들어 주고, str로 key를 취하는 느낌
#이후에 join해서 string으로 출력
#solution([0,0,0,0]) 이건 따로 0으로 나오도록 설정정
def solution(numbers):
    #문자 형식으로 리스트에 넣기 ex) ['6','10','2']
    numbers=list(map(str,numbers)) 
    #한 자리수에 대한 고민 해결
    #key=str이 아니라, lambda x: x*3으로 하기(1000이하 세 자리까지 맞춤), 1000이하로 맞추기, 오름차순
    #lambda x: x*3 : ['666','101010','222'] 
    #-> 문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교
    #만약 동일하면 다음 인덱스도 비교해서 정렬함함 
    #key, 내림차순 적용 시 -> ['666','101010','222']  -> ['6','2','10'] 
    numbers.sort(key = lambda x: x*3, reverse=True) 
    result = ''.join(numbers)
    #'00000'...이런 식일 경우, '0'으로 반환
    if(result[0]=='0'):
      return '0'
    else:
      return result 

    #return str(int(''.join(numbers))) #이게 훨씬 간단함

solution([6, 10, 2])
# solution([3, 30, 34, 5, 9])
# solution([232,23]) #오류 23232
# solution([212,21])
# solution([70,0,0,0,0])
# solution([0,0,0,0])

#다른 사람 풀이
# import functools

# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer

#다른 사람 풀이2
# def solution(numbers):
#     answer = ''
#     numbers = sorted(numbers, reverse=True, key=lambda  x: (str(x)*4).ljust(4))
#     for i in numbers:
#         answer += str(i)
#     if answer[0] == '0':    #모두 0인 경우 -> 테스트11
#         return '0'
#     return answer

#다른 사람 풀이3
# from functools import cmp_to_key

# def solution(numbers):
#     numbers = list(map(lambda x: str(x), numbers))
#     numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a+b >= b+a else 1))
#     answer = ''.join(numbers)

#     return str(int(answer))

"""**정렬 3번째 문제, H-Index**"""

#논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
#n편 중 h번 이상 인용된 논문 h편 이상 
#n편 중 h번 이하 인용된 논문 n-(h+alpha)편
#1 <= n <= 1000
#0 <= h <= 10000
#논문의 인용 횟수를 담은 배열 citations
#h의 최댓값이 이 과학자의 H-Index

#[3, 0, 6, 1, 5] 리스트의 요소: n , 3편 이상 인용 3편, 2편 이하 이용 2편 
#6 5 3 1 5 0
def solution(citations):
    citations.sort(reverse=True)
    for ind, citation in enumerate(citations):
        if citation <= ind :
            return ind
    return len(citations)

# H-index (내림차순) - 영창님, 재현님님
def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if citation <= idx :
            return idx
    return len(citations)
print(solution([3, 0, 6, 1, 5])) 
재현 — 오늘 오후 8:38
# H-index
def solution(citations):
    citations.sort()
    for idx , v in enumerate(citations):
        if v >= len(citations) - idx :
            return len(citations) - idx
    return 0

print(solution([3, 0, 6, 1, 5]))