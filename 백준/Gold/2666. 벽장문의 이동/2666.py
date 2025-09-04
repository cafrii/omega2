'''
2666번
벽장문의 이동 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	6611	3687	2781	56.444%

문제
n개의 같은 크기의 벽장들이 일렬로 붙어져 있고 벽장의 문은 n-2개만이 있다.
한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면) 그 벽장 앞으로 움직일 수 있다.

그림은 7개의 벽장의 예이다. 그림에서 2번 벽장과 5번 벽장이 열려있고, 나머지 벽장은 닫혀 있다.
벽장 문은 좌우 어느 쪽이든 그 이웃 벽장이 열려 있다면 그 쪽으로 한 칸씩 이동할 수 있다.
그림에서 주어진 상태에서는 1번 벽장을 닫고 있는 벽장문을 오른쪽으로 한 칸 이동함으로써 1번 벽장을 사용할 수 있다.
이때 2번 벽장은 닫혀져 사용할 수 없다.
역시 5번 벽장이 열려 있으므로 4번 벽장 또는 6번 벽장 앞의 벽장문을 5번 벽장 앞으로 이동시킬 수 있다.

풀어야 할 문제는 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서를 찾는 것이다.
이때 벽장문의 이동횟수를 최소로 하여야 한다.
입력은 다음과 같이 주어지며, 열려있는 벽장의 개수는 항상 2개이다.

예를 들어 사용할 벽장 순서가 3 1 6 5이면, 3번 앞의 문을 2번으로 옮겨서 3번 벽장을 사용하고(문 이동횟수=1),
다음에 1번과 2번 앞에 있는 문을 오른쪽으로 하나씩 옮겨서(문 이동횟수=2) 1번 벽장을 사용하며,
6번 앞에 있는 문을 왼쪽으로 옮겨서 6번 벽장을 사용하고(문 이동횟수=1),
다시 그 문을 오른쪽으로 옮겨서 5번 벽장을 사용한다(문 이동횟수=1),
따라서 문이 이동한 횟수의 합은 5이다.

입력
첫 번째 줄에 벽장의 개수를 나타내는 3보다 크고 20보다 작거나 같은 하나의 정수,
두 번째 줄에 초기에 열려있는 두 개의 벽장을 나타내는 두 개의 정수,
그리고 세 번째 줄에는 사용할 벽장들의 순서의 길이(최대 20),
그리고 그 다음줄부터 사용할 벽장의 번호가 한줄에 하나씩 순서대로 주어진다.

출력
벽장문의 최소 이동횟수를 화면에 출력한다.


----

7:14~8:10


'''


import sys
from heapq import heappush,heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip()) # number of door, 4~20
    assert 3<N<=20, "wrong N"
    a,b = map(int, input().split()) # door id which is initially open
    assert 1<=a<=N and 1<=b<=N, "wrong a,b"
    M = int(input().rstrip())
    assert 0<=M<=20, "wrong M"
    K = []
    for _ in range(M):
        K.append(int(input().rstrip()))
        assert 1<=K[-1]<=N, "wrong K"
    return N,a,b,K


def solve_bfs(N:int, a:int,b:int, K:list[int])->int:
    '''
    변형된 bfs. 우선순위 큐 사용
    Returns:
        minumum move count
    '''

    que = [ (0,0,a,b) ]
    # element: ( move_count, step, open_door_1, open_door_2 )
    cnt = 0

    while que:
        cnt,step,a,b = heappop(que)
        a,b = min(a,b),max(a,b)

        log("(%d) <%d,%d> cnt %d, que sz %d", step, a,b, cnt, len(que))

        if step >= len(K):
            break

        k = K[step] # target of this step

        if k == a or k == b:
            heappush(que, (cnt, step+1, a, b))
        elif k < a: #  k  a  b
            heappush(que, (cnt+(a-k), step+1, k, b))
        elif b < k: # a b k
            heappush(que, (cnt+(k-b), step+1, a, k))
        else: #if a < k < b:
            # 지금 어느 쪽 문을 사용하는 것이 더 유리한지는 알 수 없음. 두 가지 경우를 다 계산.
            heappush(que, (cnt+(k-a), step+1, k, b))
            heappush(que, (cnt+(b-k), step+1, a, k))


    log("remaining que: %d", len(que))
    return cnt


if __name__ == '__main__':
    print(solve_bfs(*get_input()))


'''
예제 입력 1
7
2 5
4
3
1
6
5
예제 출력 1
5

---
run=(python3 2666.py)

echo '7\n2 5\n4\n3\n1\n6\n5' | $run
# 5

echo '20\n1 19\n20\n5\n8\n1\n9\n4\n4\n6\n9\n10\n12\n9\n9\n1\n11\n12\n5\n20\n9\n11\n18' | $run
# 57

echo '20\n1 19\n20\n9\n20\n14\n18\n14\n8\n12\n6\n18\n16\n9\n18\n11\n19\n19\n5\n1\n7\n1\n11' | $run
# 68

echo '5\n2 3\n4\n1\n4\n1\n5' | $run
# 3

echo '20\n1 20\n10\n10\n1\n10\n1\n10\n1\n10\n1\n10\n1' | $run
# 10



'''

