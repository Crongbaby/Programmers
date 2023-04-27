# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(board, moves): #와...한번에 풀었따 ㅎ히힣.
  # 화면 : "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자
  # 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸
  # 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있음
  # 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있음
  # 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됨
  # 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됨
  # 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않음
  # board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하
  # board의 각 칸에는 0 이상 100 이하인 정수가 담김
  
  # board에서 0이 아닌 가장 위에 있는 숫자 꺼내오기.
  # moves에서 나온 숫자 - 1 = 인덱스(열)해서 가장 위에 있는 숫자 꺼내오기...  
  # stack으로 풀어야할거 같은데
  # 위 아래가 같은 숫자면 카운트하고 삭제하기

  stack = [] 
  count = 0 

  for doll in range(len(moves)):
    for rows in range(len(board)):
      
      if(board[rows][moves[doll]-1] != 0):
        stack.append(board[rows][moves[doll]-1])
        board[rows][moves[doll]-1] = 0 #바구니로 나간거 표시
        break

    if (len(stack) >=2 and stack[-2] == stack[-1]):
      stack.pop()
      stack.pop()
      count = count + 2

  return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# 다른 사람의 풀이1..나의 풀이와 거의 비슷함.
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

#다른 사람의 풀이2.

# 2번째 줄을 보면, zip(*board)를 함으로써, 원래 board의 각 원소들은 행을 나타내는 리스트들이었는데, 
# *board를 하니까 각 행을 나타내는 리스트가 그 개수만큼 unpacking됨.
# 그렇게 그 각 행을 나타내는 리스트들이 병렬로 존재하고 있는데 거기에 zip을 하니까, 
# 각 행을 나타내고 있던 리스트들의 앞부분부터 끝부분까지를 하나씩 뱉어낸 걸 모아서 새로운 리스트를 만듦.
# 한 행의 입장에서 앞부분부터 끝부분까지라는 말은, 1열부터 마지막열까지를 의미함.
# 그러므로 각 행들의 1열부터 마지막열까지를 받은 것이므로 zip(*board)는 결국 각 열을 나타내는 리스트들을 가지고 있음.
# 그런데 여기에 map을 통해서 각 열에 대해 lambda를 두 번 사용한 함수를 적용시켜줌.
# lambda x에서는 열을 나타내는 리스트를 x로 받겠다는 것이고, 열을 나타내는 리스트를 받아서 
# 그 리스트 안에 있는 각각의 값(인형)들을 y로 받아서 0보다 큰 값들만 살려줌.
# 이 문제에서 0은 인형이 없는 경우이므로 결국에는 2번째 cols = (...)줄을 마치고 나면 cols에는 
# 0번째 원소에는 첫번째 열에 위치한 실재하는 인형들을 나타내는 리스트, 1번째 원소에는 두번째 열을=에 위치한 실재하는 인형들을 나타내는 리스트 이런식으로 넣어지게 됨.
# 그리고 s는 bucket의 역할을 하고, a는 터뜨려진 인형의 수를 의미함.
# s에 처음에 [0]을 넣어주는 이유는 빈 리스트에서 s.pop()을 하면 에러가 발생하므로 그걸 방지하기 위해서 0에 해당하는 인형은 없기 때문에 넣어준 것으로, 
# 에러 발생 방지 이외의 목적은 없다. for m in moves: 안을 살펴보면, cols안의 1번째 열을 나타내는 리스트의 첫번째 원소는 그림 상으로 맨 위에 위치해있던 인형이 있고, 
# 마지막 원소는 가장 바닥에 있어야 할 인형이 있다. 그러므로 cols[m - 1].pop(0)을 하여 위에 있는 것을 빼줌
# 결국, moves에서 이번에 격자 상에서 가져오는 인형과 버킷의 맨 위에 있던 인형의 값을 비교해준다. 
# 그래서 그 둘이 같으면 인형이 터지는 것이므로 a에 2를 더해줌
# 그런데 그 둘이 다르면, 현재 버킷의 맨 위에 있던 것을 빼왔기 때문에 그 인형이 버킷의 더 깊숙한 곳에 있어야 하므로 l을 앞에 해주고, 
# 이번에 뽑은 인형 d가 뒤에 있어야 하니까 [l, d]로 만들어서 기존의 버킷에 다시 추가

def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a