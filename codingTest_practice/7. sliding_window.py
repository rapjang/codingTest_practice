checkList = [0]*4
myList = [0]*4
checkSecret = 0

# 함수정의

# 새로 들어온 문자를 처리하는 함수
def myadd(c):
    global checkList, myList, checkSecret
    if c == "A":
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == "C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == "G":
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

#제거되는 문자를 처리하는 함수
def myremove(c):
    global checkList, myList, checkSecret
    if c == "A":
        if myList[0] == checkList[0]:
            checkSecret -= 1
    elif c == "C":
        if myList[1] == checkList[1]:
            checkSecret -= 1
    elif c == "G":
        if myList[2] == checkList[2]:
            checkSecret -= 1
    elif c == "T":
        if myList[3] == checkList[3]:
            checkSecret -= 1
            
S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1
    
# 초기 P부분 문자열 처리 부분    
for i in range(P):
    myadd(A[i])
    
# 4 자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
if checkSecret == 4:
    Result += 1

for i in range(P, 5):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)
    