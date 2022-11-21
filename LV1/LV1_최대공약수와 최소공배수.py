# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(n, m):
  result = []
  result.append(max([i for i in range(min(n,m),0,-1) if(n%i==0 and m%i==0)])) #최대공약수
  result.append(min([i for i in range(max(n,m),(n*m)+1) if(i%n==0 and i%m==0)])) #최소공배수
  return result
print(solution(3,12))
print(solution(2,5))

#다른 사람의 풀이1...
#while d: c, d = d, c % d 로 하면 t 안 쓸 수 있습니다.
#from math import gcd 사용하면 될 듯듯
def gcdlcm(a, b): 
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

#다른 사람의 풀이2
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]

#다른 사람의 풀이3...
def gcdlcm(a, b):
    for i in range(a):
        if a%(a-i)+b%(a-i) == 0:
            return [a-i, a*b/(a-i)]