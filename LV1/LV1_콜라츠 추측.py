# -*- coding: utf-8 -*-
"""Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c75-Cr0TfQuGgHxqaIJ0bE00EscZMsOS
"""

def solution(num):
    count = 0
    while True: 
        if(num == 1):
            break
        elif(num % 2 == 0):
            num /=  2
            count+=1
        else:
            num = num * 3 + 1
            count+=1
    #[참일 경우 value] if [조건식] else [거짓일 경우 value]
    return (count if 500 > count else -1) 

print(solution(6))
print(solution(16))
print(solution(626331))

#삼항 연산자를 생각해보니 또 사용해도 되는 것을...
# def collatz(num):
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num*3 + 1
#         if num == 1:
#             return i + 1
#     return -1

#애초에 무한 루프 조건식에서 1이 아닌 조건을 넣으면 되었었는데...
# def collatz(num):
#     answer = 0
#     while num!=1:
#         if num%2==0:
#             num=num/2
#         else:
#             num=3*num+1
#         answer=answer+1

#         if answer>=500:
#             return -1

#     return answer