# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

import string
def solution(n):
  def convert_notation(n, base): #10진수를 n진수로 변환
    T = "0123456789ABCDEF"
    q, r = divmod(n, base) #몫, 나머지 튜플 형식으로 넣어줌
    return convert_notation(q, base) + T[r] if q else T[r]
  return int(str(convert_notation(n, 3))[::-1],3) #int(str,n) 10진수로 변환

print(solution(45))
#print(solution(125))

#다른 사람의 풀이1....
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

#다른 사람의 풀이2...
def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    print(a)
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer