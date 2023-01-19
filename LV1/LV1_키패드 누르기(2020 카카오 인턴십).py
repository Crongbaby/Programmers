# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

import numpy as np
import math #유클리드때 필요했는데 테스트 13부터 틀리면 맨허튼 거리로 하라고해서 필요없어짐.
def solution(numbers, hand): #2일동안 3시간씩 뒤져서 푼 나의 역작...ㅎ. 
  
  def distance(x1, y1, x2, y2):
    #result = math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) #유클리드
    result = abs(x1 - x2) + abs(y1 - y2) #맨허튼 거리
    return result

  phone = [[1,2,3],   
           [4,5,6],
           [7,8,9],
           ['*',0,'#']] #키보드 2차원 배열
  phone_numpy = np.array(phone)

  result = ''
  L_hand_pos = '*' #왼손 위치 
  R_hand_pos = '#' #오른손 위치

  for i in numbers:

    print('i: ',i)
    print('L_hand_pos: ',L_hand_pos)
    print('R_hand_pos: ',R_hand_pos)

    if(str(i) in '147'):
      result += 'L'
      L_hand_pos = i
    elif(str(i) in '369'):
      result += 'R'
      R_hand_pos = i
    else: #문자로해야함
      x_num = np.where(phone_numpy == str(i))[0][0]
      y_num = np.where(phone_numpy == str(i))[1][0]
      x_L = np.where(phone_numpy == str(L_hand_pos))[0][0]
      y_L = np.where(phone_numpy == str(L_hand_pos))[1][0]
      x_R = np.where(phone_numpy == str(R_hand_pos))[0][0]
      y_R = np.where(phone_numpy == str(R_hand_pos))[1][0]

      if(distance(x_num,y_num,x_L,y_L) < distance(x_num,y_num,x_R,y_R)): 
        result += 'L'
        L_hand_pos = i
      elif(distance(x_num,y_num,x_L,y_L) > distance(x_num,y_num,x_R,y_R)): 
        result += 'R'
        R_hand_pos = i
      else:
        if(hand == "left"):
          result += 'L'
          L_hand_pos = i
        else:
          result += 'R'
          R_hand_pos = i

      print('result: ',result)

  return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))

#다른 사람의 풀이1. 나와 거의 비슷함 여기서는 딕셔너리로 했네..ㅎ.
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

#다른 사람의 풀이2...거리를 저장해버리는 ....ㅋㅋㅋㅋㅋ정성 가득이네.
def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer

#다른 사람의 풀이3..n손잡이 가능성을 생각을...

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def solution(numbers, hand):
    answer = ''
    location = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left, right = [3, 0], [3, 2]
    for i in numbers:
        if i % 3 == 1:
            answer += 'L'
            left = location[i]
        elif i % 3 == 0 and i != 0:
            answer += 'R'
            right = location[i]
        else:
            l = abs(location[i][0] - left[0]) + abs(location[i][1] - left[1])
            r = abs(location[i][0] - right[0]) + abs(location[i][1] - right[1])
            if l < r:
                answer += 'L'
                left = location[i]
            elif l > r:
                answer += 'R'
                right = location[i]
            else:
                answer += hand[0].upper()
                if hand == 'right':
                    right = location[i]
                else:
                    left = location[i]                

    return answer