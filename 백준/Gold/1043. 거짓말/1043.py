'''
1043번
거짓말 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	43637	20145	15543	46.357%

문제
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다.
지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다.
당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다.
하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다.
문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다.
따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다.
당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도
지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다.
그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다.
이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다.
진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다.
사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수,
각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

---------

4:35~5:42  중간 휴식 시간 등.

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    tt = list(map(int, input().split())) # those who know truth: [num, ...]
    # assert tt[0] == len(tt)-1, "wrong a format"
    del tt[0]
    parties = []
    for _ in range(M):
        gg = list(map(int, input().split()))
        # assert gg[0] == len(gg)-1, "wrong gg format"
        parties.append(gg[1:])
    return N,tt,parties

def solve(N:int, tt:list[int], parties:list[list[int]])->int:
    '''
        tt: 진실을 아는 사람 목록
    '''
    # log("tt %s", tt)
    roots = list(range(N+1))

    def find_root(a:int)->int:
        # 요소 a 가 속한 집합의 대표값을 리턴
        if a == roots[a]: return a
        roots[a] = find_root(roots[a])
        return roots[a]

    # 번호 0은 사용되지 않으므로, 진실 그룹의 초기 대표자로 지정.
    ra = 0
    for b in tt:
        rb = find_root(b)
        if ra == rb: continue
        roots[rb] = roots[b] = ra

    # log("#..: %s", roots)

    for guests in parties:
        # 파티에 참석한 게스트들은 모두 한 그룹에 소속되게 됨.
        if len(guests) <= 1: continue
        a,ra = guests[0],find_root(guests[0])
        for b in guests[1:]:
            rb = find_root(b)
            if ra == rb: continue
            if rb == 0: roots[ra] = roots[a] = 0
            else: roots[rb] = roots[b] = ra

    return [ find_root(g[0])>0 for g in parties ].count(True)


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)



'''
예제 입력 1
4 3
0
2 1 2
1 3
3 2 3 4
예제 출력 1
3

예제 입력 2
4 1
1 1
4 1 2 3 4
예제 출력 2
0

예제 입력 3
4 1
0
4 1 2 3 4
예제 출력 3
1

예제 입력 4
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
예제 출력 4
2

예제 입력 5
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4
예제 출력 5
4

예제 입력 6
8 5
3 1 2 7
2 3 4
1 5
2 5 6
2 6 8
1 8
예제 출력 6
5

예제 입력 7
3 4
1 3
1 1
1 2
2 1 2
3 1 2 3
예제 출력 7
0

run=(python3 1043.py)

echo '4 3\n0\n2 1 2\n1 3\n3 2 3 4' | $run
# 3
echo '4 1\n1 1\n4 1 2 3 4' | $run
# 0
echo '4 1\n0\n4 1 2 3 4' | $run
# 1
echo '4 5\n1 1\n1 1\n1 2\n1 3\n1 4\n2 4 1' | $run
# 2
echo '10 9\n4 1 2 3 4\n2 1 5\n2 2 6\n1 7\n1 8\n2 7 8\n1 9\n1 10\n2 3 10\n1 4' | $run
# 4
echo '8 5\n3 1 2 7\n2 3 4\n1 5\n2 5 6\n2 6 8\n1 8' | $run
# 5
echo '3 4\n1 3\n1 1\n1 2\n2 1 2\n3 1 2 3' | $run
# 0



'''
