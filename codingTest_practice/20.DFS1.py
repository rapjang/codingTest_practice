import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
# n : 노드개수 / m : 에지개수
n, m = map(int, input().split())
# A : 그래프 데이터 저장 인접 리스트 초기화
A = [[] for _ in range(n+1)]
# visted : 방문기록리스트 초기화
visted = [False] * (n+1)

# DFS구현
def DFS(v):
    # visted 리스트에 현재 노드 방문 기록
    visted[v] = True
    # 현재 노드의 연결 노드 중
    # 방문하지 않은 노드로 DFS실행 (재귀함수형태)
    for i in A[v]:
        if not visted[i]:
            DFS(i)

# A 인접 리스트에 그래프데이터 저장
for _ in range(m):
    s,e = map(int, input().split())
    # 양방향에지이므로 양쪽에 에지를 더하기
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1,n+1):
    # 연결 노드 중 방문하지 않았던 노드만 탐색
    # 방문하지 않은 노드가 있으면
    # 연결 요소 개수 값 1 증가
    # DFS실행
    if not visted[i]:
        count += 1
        DFS(i)
        
print(count)