# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(n):
  arr = ["수", "박"]; new = []
  for i in range(n):
    new.append(arr[1]) if(i%2==1) else new.append(arr[0])
  result = ''.join(s for s in new)
  return result

print(solution(3))
print(solution(4))

#다른 사람 풀이
# def water_melon(n):
#     s = "수박" * n
#     return s[:n]

# def water_melon(n):
#     return "수박"*(n//2) + "수"*(n%2)

# def water_melon(n):
#     return ("수박"*n)[0:n]

# def solution(n):
#     return "".join(["수박"[i%2] for i in range(n)])