# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

#런타임 에러난 화나는 코드..
#index 함수를 남발해서 이렇게 된 것 같음... 안 써야지
def solution(s, n): #a->a: 25, a->z: 24
  new_alpha = []
  for i in s:
    if i == " ":
      new_alpha.append(i)
    else: 
      if i.isupper() and ord(i)+n > 90:
        new_alpha.append(chr(64+((ord(i)+n)-90)))
      elif i.islower() and ord(i)+n > 122:
        new_alpha.append(chr(96+((ord(i)+n)-122)))
      else:
        new_alpha.append(chr(ord(i)+n))
  return ''.join(new_alpha)

print(solution("AB",1)) 
print(solution("z",1)) 
print(solution("a B z",4))
print( solution("AaZz", 25))
print(solution("a    b", 1))
print(solution("a b ", 1))
print(solution("bC",25))

#다른 사람 풀이1...
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)