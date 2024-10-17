# 인접 리스트로 그래프 표현
graph = {
    0: [1, 4],  # 0번 노드와 연결된 노드들
    1: [0, 3],  # 1번 노드와 연결된 노드들
    2: [3],     # 2번 노드와 연결된 노드들
    3: [1, 2, 4],  # 3번 노드와 연결된 노드들
    4: [0, 3]   # 4번 노드와 연결된 노드들
}

# 방문한 노드를 기록하는 리스트
visited = [False] * 5  # 노드가 0 ~ 4번까지 총 5개이므로 크기 5로 설정

# 방문 순서를 저장할 리스트
visit_order = []

# DFS 함수 (스택 기반)
def dfs_stack(start):
    stack = [start]  # 시작 노드를 스택에 넣음
    visited[start] = True  # 시작 노드 방문 처리

    while stack:
        node = stack.pop()  # 스택에서 노드를 하나 꺼냄
        visit_order.append(node)  # 방문 순서를 기록

        # 인접한 노드들을 차례대로 스택에 넣음 (방문하지 않은 노드만)
        for neighbor in reversed(graph[node]):  # 순서를 유지하기 위해 역순으로 삽입
            # stack이니깐 LIFO로 마지막에 넣은 것이 가장 최근으로 뽑혀 나오기 때문에 역전해야 한다.
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True  # 스택에 넣을 때 방문 처리

# DFS 탐색 시작 (0번 노드에서 시작)
dfs_stack(0)

# 방문한 순서 출력
print("방문 순서:", visit_order)
