'''
20040번
사이클 게임 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	24270	12995	9659	50.447%

문제
사이클 게임은 두 명의 플레이어가 차례대로 돌아가며 진행하는 게임으로,
선 플레이어가 홀수 번째 차례를, 후 플레이어가 짝수 번째 차례를 진행한다.

게임 시작 시 0 부터 n-1 까지 고유한 번호가 부여된 평면 상의 점 n 개가 주어지며,
이 중 어느 세 점도 일직선 위에 놓이지 않는다.

매 차례 마다 플레이어는 두 점을 선택해서 이를 연결하는 선분을 긋는데,
이전에 그린 선분을 다시 그을 수는 없지만 이미 그린 다른 선분과 교차하는 것은 가능하다.
게임을 진행하다가 처음으로 사이클을 완성하는 순간 게임이 종료된다.

사이클 C는 플레이어가 그린 선분들의 부분집합으로, 다음 조건을 만족한다.
- C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.

문제는 선분을 여러 개 그리다 보면 사이클이 완성 되었는지의 여부를 판단하기 어려워
이미 사이클이 완성되었음에도 불구하고 게임을 계속 진행하게 될 수 있다는 것이다.
이 문제를 해결하기 위해서 게임의 진행 상황이 주어지면 몇 번째 차례에서 사이클이 완성되었는지,
혹은 아직 게임이 진행 중인지를 판단하는 프로그램을 작성하려 한다.

입력으로 점의 개수 n과 m 번째 차례까지의 게임 진행 상황이 주어지면 사이클이 완성 되었는지를 판단하고,
완성되었다면 몇 번째 차례에서 처음으로 사이클이 완성된 것인지를 출력하는 프로그램을 작성하시오.

입력
입력은 표준입력을 사용한다. 입력의 첫 번째 줄에는 점의 개수를 나타내는 정수 3 ≤ n ≤ 500,000 과
진행된 차례의 수를 나타내는 정수 3 ≤ m ≤ 1,000,000 이 주어진다.
게임에서 사용하는 n개의 점에는 0 부터 n-1 까지 고유한 번호가 부여되어 있으며,
이 중 어느 세 점도 일직선 위에 놓이지 않는다.
이어지는 m 개의 입력 줄에는 각각 i번째 차례에 해당 플레이어가 선택한 두 점의 번호가 주어진다 (1 ≤ i ≤ m).

출력
출력은 표준출력을 사용한다. 입력으로 주어진 케이스에 대해, m 번째 차례까지 게임을 진행한 상황에서
이미 게임이 종료되었다면 사이클이 처음으로 만들어진 차례의 번호를 양의 정수로 출력하고,
m 번의 차례를 모두 처리한 이후에도 종료되지 않았다면 0을 출력한다.

-----

8:14~21 중지.
10:23~11:00 ?

아래는 최종 제출본.
링크 정보 저장을 위해 메모리 할당 하지 않음.
대신 입력부, 계산부 분리를 위해 generator 사용.

'''

import sys
from typing import Generator

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    def gen_lines()->Generator:
        for i in range(M):
            a,b = map(int, input().split())
            yield (i+1,a,b)
        return
    return (N,gen_lines())


def solve(N:int, g:Generator[tuple[int,int,int]]):
    '''
    '''
    parent = [ k for k in range(N) ]
    # parent[k] 는 노드 k 의 parent.
    # 자기 자신이 parent 라면 그 트리는 단독 노드 상태. (single node tree)

    depth = [0] * N
    # depth[k] 는 node-k 를 root로 하는 트리의 깊이 (높이)
    # 단독 노드 트리는 깊이 0 이라고 정의하자.

    def find_root(node:int)->int:
        # 지정한 노드가 속한 트리의 root 를 찾아서 리턴.
        # while node != parent[node]:
        #     node = parent[node]
        if node != parent[node]:
            parent[node] = find_root(parent[node])
            # 한번 찾아 둔 root는 parent[]에 저장해 둠.
        return parent[node]

    for idx,a,b in g:
        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            # log("(%d) %d %d, same root %d", idx, a, b, root_a)
            return idx

        # 그냥 두 트리를 연결하면 되는데 depth를 최소화 하면 find_root 속도가 개선됨.
        # 작은 트리를 큰 트리의 서브로 이으면 크기가 더 커지지 않음.
        if depth[root_a] > depth[root_b]:
            # a 가 더 큰 트리
            parent[root_b] = root_a
        elif depth[root_a] < depth[root_b]:
            parent[root_a] = root_b
        else: # 두 트리의 크기가 같으면 아무 쪽이나 연결하고, 대신 트리 크기 갱신 필요함.
            parent[root_b] = root_a # a 아래에 b를 추가.
            depth[root_a] += 1

        # log("(%d) %d %d, root %d %d", idx, a, b, root_a, root_b)

    # if cycle not detected, return 0
    return 0


if __name__ == '__main__':
    inp = get_input()
    print(solve(*inp))


'''
예제 입력 1
6 5
0 1
1 2
2 3
5 4
0 4
예제 출력 1
0
예제 입력 2
6 5
0 1
1 2
1 3
0 3
4 5
예제 출력 2
4

run=(python3 20040.py)

echo '6 5\n0 1\n1 2\n2 3\n5 4\n0 4' | $run
echo '6 5\n0 1\n1 2\n1 3\n0 3\n4 5' | $run
->
0
4





'''
