import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
# N : 노드개수, M : 에지개수
N, M = map(int, input().split())
# 도착확인변수
arrive = False
# A : 그래프 데이터 저장 인접리스트
A = [[] for _ in range(N+1)]
# 방문기록 저장 리스트
visited = [False] * (N+1)

def DFS(now, depth):
    global arrive
    # 깊이가 5가되면 종료
    if depth == 5:
        arrive = True
        return
    # 방문리스트에 현재노드 방문 기록
    visited[now] = True
    # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS실행
    # 호출마다 depth는 1씩 증가
    for i in A[now]:
        if not visited[i]:
            # 재귀 호출마다 깊이 증가
            DFS(i, depth+1)
    visited[now] = False

for _ in range(M):
    # A 인접 리스트에 그래프 데이터 저장
    s, e = map(int, input().split())
    # 양방향 에지이므로 양쪽에 에지 더하기
    A[s].append(e)
    A[e].append(s)

for i in range(N):
    # 노드마다 DFS실행
    DFS(i,1)
    # depth가 5에 도달한 적이 있다면
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)
    