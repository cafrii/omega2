
'''
스택 2
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	1024 MB	46553	17137	14153	37.072%
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
입력
첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

출력을 요구하는 명령은 하나 이상 주어진다.

출력
출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

주의 사항:
기본 i/o 를 사용할 경우 시간 초과가 발생하게 되어 있음.


https://www.acmicpc.net/problem/15552

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

'''
import sys
input = sys.stdin.readline

N = int(input().rstrip())

stack = []

for i in range(N):
    s = list(map(int, input().rstrip().split()))

    if s[0] == 1:
        stack.append(s[1]) if len(s) == 2 else None
    elif s[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif s[0] == 3:
        print(len(stack))
    elif s[0] == 4:
        print(0) if stack else print(1)
    elif s[0] == 5:
        print(stack[-1]) if stack else print(-1)


'''
예제 입력 1
9
4
1 3
1 5
3
2
5
2
2
5

예제 출력 1
1
2
5
3
3
-1
-1

'''