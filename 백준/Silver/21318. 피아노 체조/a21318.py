'''
21318번
피아노 체조 성공  실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	1024 MB	3819	1882	1556	49.054%

문제
피아노를 사랑하는 시은이는 매일 아침 피아노 체조를 한다.
시은이는 N개의 악보를 가지고 있으며, 1번부터 N번까지의 번호로 부른다.
각 악보는 1 이상 109 이하의 정수로 표현되는 난이도를 가지고 있다.
난이도를 나타내는 수가 클수록 어려운 악보이다.
1 ≤ x ≤ y ≤ N 을 만족하는 두 정수 x, y를 골라 x번부터 y번까지의 악보를 번호 순서대로 연주하는 것이 피아노 체조이다.

시은이는 피아노 체조를 할 때, 지금 연주하는 악보가 바로 다음에 연주할 악보보다 어렵다면 실수를 한다.
다시 말하자면, i(x ≤ i < y)번 악보의 난이도가 i + 1번 악보의 난이도보다 높다면 실수를 한다.
특히, 마지막으로 연주하는 y번 악보에선 절대 실수하지 않는다.
시은이는 오늘도 피아노 체조를 하기 위해 두 정수 x와 y를 골랐고, 문득 궁금한 것이 생겼다.
오늘 할 피아노 체조에서 실수하는 곡은 몇 개나 될까?

입력
첫 번째 줄에 악보의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.

두 번째 줄에 1번 악보부터 N번 악보까지의 난이도가 공백을 구분으로 주어진다.

세 번째 줄에 질문의 개수 Q(1 ≤ Q ≤ 100,000)이 주어진다.

다음 Q개의 줄에 각 줄마다 두 개의 정수 x, y(1 ≤ x ≤ y ≤ N)가 주어진다.

출력
x번부터 y번까지의 악보를 순서대로 연주할 때, 몇 개의 악보에서 실수하게 될지 0 이상의 정수 하나로 출력한다. 각 출력은 개행으로 구분한다.

----

8:00~8:35


'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    Q = int(input().rstrip())
    B = [ list(map(int, input().split()))  for _ in range(Q) ]
    return A,B


def solve(A:list[int], B:list[list[int]])->list[int]:
    '''
    Args: A: 주어진 숫자 배열, B: 검사할 범위 [x,y]의 목록
    Returns: 주어진 각 x,y 범위에서의 감소 횟수의 목록
    '''
    log("A: %s", A)

    N = len(A)
    delta = [0]*(N)
    # delta[k]는 첫번째 악보(A[0])부터 k번째 악보(A[k])까지의 범위 (즉 A[0:k+1]) 에서
    # 감소하는 요소의 (누적) 개수
    #
    for k in range(1,N):
        if A[k-1] > A[k]:
            delta[k] = delta[k-1] + 1
        else:
            delta[k] = delta[k-1]
    log("delta: %s", delta)

    ans = [ delta[y-1] - delta[x-1] for x,y in B ]
    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))


'''
예제 입력 1
9
1 2 3 3 4 1 10 8 1
5
1 3
2 5
4 7
9 9
5 9
예제 출력 1
0
0
1
0
3
예제 입력 2
6
573 33283 5572 346 906 567
5
5 6
1 3
2 2
1 6
3 6
예제 출력 2
1
1
0
3
2

----
run=(python3 a21318.py)

echo '9\n1 2 3 3 4 1 10 8 1\n5\n1 3\n2 5\n4 7\n9 9\n5 9' | $run
# 0  0  1  0  3

echo '6\n573 33283 5572 346 906 567\n5\n5 6\n1 3\n2 2\n1 6\n3 6' | $run
# 1  1  0  3  2

echo '1\n100\n2\n1 1\n1 1' | $run
# 0  0



'''
