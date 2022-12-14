# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

from itertools import permutations #파이썬으로 모든 조합 구하기
import math
def solution(numbers):
  number = list(map(str, numbers)) #문자열 리스트로 변환
  num_combin_1= list(permutations(number, 1)) #모든 조합
  num_combin_2= list(permutations(number, 2)) #모든 조합
  num_combin_3= list(permutations(number, 3)) #모든 조합
  num_combin_4= list(permutations(number, 4)) #모든 조합
  num_combin_5= list(permutations(number, 5)) #모든 조합
  num_combin_6= list(permutations(number, 6)) #모든 조합
  num_combin_7= list(permutations(number, 7)) #모든 조합
  num_int=[]; result=[];

  for i in num_combin_1: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))

  for i in num_combin_2: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))

  for i in num_combin_3: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))

  for i in num_combin_4: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))

  for i in num_combin_5: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))

  for i in num_combin_6: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))

  for i in num_combin_7: #문자열로 만들고 정수로 만들기 ex) [('1', '7')] -> "17" -> 17
    num_int.append(int(''.join(s for s in i)))
  num_int = list(set(num_int)) #중복 제거하기

  #소수인지 아닌지 판별
  for ele in num_int:
    if ele < 2:
      continue
    is_prime = True
    for j in range(2, ele):
      if ele % j == 0:
        is_prime = False
        break
    if is_prime:
      result.append(ele)
        
  return(len(result))

print(solution("17"))
print(solution("011"))
#print(solution("1234"))

#다른 사람 풀이1 -> 내 풀이를 매우 간소화 할 수 있는.......
#에라토스테네스 체를 set을 이용해서 씀..

# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)

#다른 사람 풀이2 ->재귀함수를 이용한 풀이..ㅎㅎ

# primeSet = set()


# def isPrime(number):
#     if number in (0, 1):
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False

#     return True


# def makeCombinations(str1, str2):
#     if str1 != "":
#         if isPrime(int(str1)):
#             primeSet.add(int(str1))

#     for i in range(len(str2)):
#         makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


# def solution(numbers):
#     makeCombinations("", numbers)

#     answer = len(primeSet)

#     return answer