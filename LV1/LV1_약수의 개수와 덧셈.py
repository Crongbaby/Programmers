# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(left, right):
  def count_fun(n):
    count = 0
    for i in range(1,n+1):
      if(n%i==0): 
        count += 1
    return count
  return sum([-i if(count_fun(i)%2==1) else i for i in range(left,right+1)])

print(solution(13,17))
print(solution(24,27))

#다른 사람의 풀이1..수학적 접근..
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5: #제곱수는 약수의 개수가 홀수
#             answer -= i 
#         else:
#             answer += i
#     return answer

#다른 사람 풀이2....
# def solution(left, right):
#     answer = sum([pow(-1,len([n for n in range(1, k//2+1) if k % n ==0])+1)*k for k in range(left,right+1)])
#     return answer