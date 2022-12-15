# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(s): #교양 파이썬에서 배운 딕셔너리 사용해보기
  num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
  for key in num_s:
    if key in s:
      s.replace(key,str(num_s[key]))
      s = s.replace(key,str(num_s[key]))  
  return int(s)
print(solution("one4seveneight")) 
print(solution("23four5six7")) 
print(solution("2three45sixseven")) 
print(solution("123")) 

#다른 사람 풀이1...다 item() 함수를 사용하네
# items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있음
#튜플로 받음
#car = {"name" : "BMW", "price" : "7000"}; car.items() 
#dict_items([('name', 'BMW'), ('price', '7000')]) 
def solution(s):
    answer = s 
    num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for item in num_s.items():
        answer = answer.replace(item[0], str(item[1]))   


    return int(answer)

#다른 사람의 풀이2..
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

#나의 방법과 가장 비슷한 다른 사람의 풀이3
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)