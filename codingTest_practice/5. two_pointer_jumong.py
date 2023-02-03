import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
i = 0
j = N-1

# 투 포인터 이동 원칙 따라 포인터를 이동하여 처리
while i < j :
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count +=1
        i +=1
        j -=1
        
print(count)
