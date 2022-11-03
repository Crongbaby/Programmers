# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(answers):
  hatemath_1=[1,2,3,4,5]*2000; hatemath_2=[2,1,2,3,2,4,2,5]*1250; hatemath_3=[3,3,1,1,2,2,4,4,5,5]*1000; result = []; 
  result.append(len([i for i, j in zip(answers, hatemath_1) if i == j]))
  result.append(len([i for i, j in zip(answers, hatemath_2) if i == j]))
  result.append(len([i for i, j in zip(answers, hatemath_3) if i == j]))
  return list(i+1 for i in range(3) if max(result) == result[i])

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

#다른 사람 풀이1
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result

#다른 사람 풀이2
# def solution(answers):
#     p = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     s = [0] * len(p)

#     for q, a in enumerate(answers):
#         for i, v in enumerate(p):
#             if a == v[q % len(v)]:
#                 s[i] += 1
#     return [i + 1 for i, v in enumerate(s) if v == max(s)]

#다른 사람 풀이3
# from itertools import cycle

# def solution(answers):
#     giveups = [
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0]
#     for num in answers:
#         for i in range(3):
#             if next(giveups[i]) == num:
#                 scores[i] += 1
#     highest = max(scores)

#     return [i + 1 for i, v in enumerate(scores) if v == highest]

#다른 사람 풀이4
# def solution(e):
#     a=[0]*3;c=[2,1,2,3,2,4,2,5];d=[3,1,2,4,5]
#     for i in range(0,len(e)):z=e[i];a[0]+=range(1,6)[i%5]==z;a[1]+=c[i%8]==z;a[2]+=d[i//2%5]==z
#     return[i+1 for i in range(0,3)if a[i]==max(a)]