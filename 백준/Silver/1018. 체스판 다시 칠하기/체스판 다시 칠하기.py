# # 체스판 크기 입력 받고
# n, m = map(int, input().split())

# board = []

# # 세로 길이 만큼 반복하며 현황 입력 받음
# for _ in range(n):
#   row = list(input())
#   board.append(row)

# # answer 초기값은 일단 8 * 8 일 때 최악의 경우인 32로 세팅
# answer = 32

# # 색상 변경하는 함수 정의
# def color_change(copy_board):

#   # 대조군은 줄마다 달리 해야하기 때문에 변수로 세팅
#   control_group = []

#   # 검은색이 먼저 오는 경우와
#   b_count = 0
  
#   for r in range(8):
#     if r % 2 == 0:
#       control_group = ['B','W','B','W','B','W','B','W']
#     else:
#       control_group = ['W','B','W','B','W','B','W', 'B']
#     for c in range(8):
#       if copy_board[r][c] != control_group[c]:
#         b_count += 1

#   # 하얀색 먼저오는 경우
#   w_count = 0
  
#   for r in range(8):
#     if r % 2 == 0:
#       control_group = ['W','B','W','B','W','B','W', 'B']
#     else:
#       control_group = ['B','W','B','W','B','W','B','W']
#     for c in range(8):
#       if copy_board[r][c] != control_group[c]:
#         w_count += 1

#   # 모두 구해서 적게 뒤집는 경우로 리턴
#   return min(b_count, w_count)

# # 보드 왼쪽 끝부터 
# # 가로든 세로든 8칸으로 잘라도 범위를 넘지 않는 곳까지 반복하며
# for r in range(0, len(board) - 7):
#   for c in range(0, len(board[0]) - 7):
#     # 8 * 8 크기로 잘라서 색깔 다 바뀌 본 다음 최소값으로 정답 갱신
#     section = [arr[c:c + 8]for arr in board[r:r + 8]]
#     change_count = color_change(section)
#     answer = min(answer, change_count)

# print(answer)

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)

print(min(repair))
