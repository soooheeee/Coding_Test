
# 인접 리스트로 그래프 표현
graph = {
  0: [1,4],
  1: [0,3],
  2: [3],
  3: [1,2,4],
  4: [0,3]
}

# 방문한 노드를 기록하는 리스트
visited = [False] * 5

# 방문 순서를 저장할 리스트
visited_order = []

# DFS 함수 정의
def dfs(node):
  visited[node] = True # 현재 노드 방문 처리
  visited_order.append(node) # 방문한 순서를 기록
  for neighbor in graph[node]:
    if not visited[neighbor]:
      dfs(neighbor)

# DFS 탐색 시작 (0번 노드에서 시작)
dfs(0)

# 방문한 순서 출력
print("방문 순서", visited_order) # [0,1,3,2,4]