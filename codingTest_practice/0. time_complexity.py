import random
findNumber = random.randrange(1,101)

for i in range(1,101):
    if i == findNumber:
        print(i)
        break


# computing count = N
N = 100000
cnt = 1
for i in range(N):
    print("연산횟수 ", str(cnt))
    cnt += 1
    
# computing count = N*N
N = 100000
cnt = 1
for i in range(N):
    for j in range(N):
        print("연산횟수 ", str(cnt))
        cnt += 1
# 커밋 확인용
