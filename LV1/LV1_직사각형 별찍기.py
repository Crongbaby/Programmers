# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

n, m = map(int, input().strip().split(' '))
for i in range(m):
    print('*'*n)

#다른 사람의 풀이1...간단하게 풀음
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

#다른 사람의 풀이2.정석...
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')