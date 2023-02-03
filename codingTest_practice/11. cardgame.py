from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

# 카드가 1장 남을 때까지
while len(myQueue) > 1:
    # 맨 위의 카드를 버림
    myQueue.popleft()
    # 맨 위의 카드를 가장 아래 카드 밑으로 이동
    myQueue.append(myQueue.popleft())
    
print(myQueue[0])