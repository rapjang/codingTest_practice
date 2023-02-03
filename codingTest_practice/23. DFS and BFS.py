from collections import deque
# N : 노드 개수 / M : 에지 개수 / Start : 시작점
N, M, Start = map(int, input().split())
# A : 그래프 데이터 저장 인접 리스트
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    # A 인접 리스트에 그래프 데이터 저장
    # 양방향 에지이므로 양쪽에 에지를 더하기
    A[s].append(e)
    A[e].append(s)
    
for i in range(N+1):
    # 각 노드와 관련된 에지를 정렬
    # 번호가 작은 노드부터 방문하기 위해 정렬하기
    A[i].sort()

def DFS(v) :
    # 현재 노드 출력
    print(v, end = ' ')
    # visited 리스트에 현재 노트 방문 기록하기
    visited[v] = True
    # 현재 노드의 연결 노드 중 방문하지 않은 노드로
    # DFS 실행하기 (재귀함수 형태)
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# visited 리스트 초기화
visited = [False] * (N+1)
# DFS실행
DFS(Start)


def BFS(v):
    # 큐 자료구조에 시작노드 삽입
    queue = deque()
    queue.append(v)
    # visited 리스트에 현재 노드 방문 기록
    visited[v] = True
    # 큐가 빌 때까지
    while queue:
        # 큐에서 노드 데이터를 가져오기
        now_Node = queue.popleft()
        # 가져온 노드 출력
        print(now_Node, end = ' ')
        # 현재 가져온 연결 노드 중 미방문 노드를
        # 큐에 삽입(append)하고 방문리스트에 기록
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (N+1)
BFS(Start)