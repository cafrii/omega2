'''
입력
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
'''

while True:
    A,B,C = map(int, input().split())
    if (A,B,C) == (0,0,0):
        break
    if A*A == B*B + C*C or \
        B*B == A*A + C*C or \
        C*C == A*A + B*B:
        print("right")
    else:
        print("wrong")

