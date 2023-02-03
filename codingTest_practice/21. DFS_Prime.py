import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
# N : 자릿수
N = int(input())

# 소수 구하기 함수
def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

def DFS(number) :
    if len(str(number)) == N:
        print(number)
    else : 
        for i in range(1,10):
            # i를 뒤에 붙인 새로운 수가 홀수이면서 소수일 때
            # DFS(수 * 10 + 뒤에 붙는 수) 실행
            # 짝수라면 더는 탐색 불필요
            if i % 2 == 0:
                continue
            # 소수이면 자릿수 늘림
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)

# DFS실행 (숫자 2,3,5,7로 탐색 시작)
# 일의자리 소수는 2,3,5,7이므로 4가지 수 에서만 시작
DFS(2)
DFS(3)
DFS(5)
DFS(7)