import sys
input = sys.stdin.readline
N = int(input()) # 정렬할 수 개수
count = [0]*10001 # 카운팅 정렬 리스트

for i in range(N):
    #count 리스트에 현재 수에 해당하는 index값 1증가
    count[int(input())] += 1

for i in range(10001):
    #i가 기존 input에 있는 수
    if count[i] != 0:
        # 해당 index값만큼 index를 반복하여 출력
        for _ in range(count[i]):
            print(i)