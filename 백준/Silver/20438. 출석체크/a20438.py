'''
20438번
출석체크 성공, 실버2

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초	1024 MB	4348	1316	988	29.136%

문제
코로나 바이러스로 인해 H 대학은 비대면 강의를 실시하고 있다.
조교를 담당하게 된 지환이는 출석체크 방식을 바꾸려고 한다.

학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다.

지환이가 한 학생에게 출석 코드를 보내게 되면,
해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석을 할 수 있게끔 한다.

하지만, K명의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.

지환이는 무작위로 한 명의 학생에게 출석 코드를 보내는 행위를 Q번 반복한 뒤,
출석부 정리를 위해 특정 구간의 입장 번호를 받은 학생들 중에서 출석이 되지 않은 학생들의 수를 구하고 싶다.

많은 인원을 담당해서 바쁜 지환이를 위해 프로그램을 만들어주자!

입력
1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q,
주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)

2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과
Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.

4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)

출력
M개의 줄에 걸쳐서 각 구간에 대해서 출석이 되지 않은 학생들의 수를 출력하라.

--------

M회 검사 반복 시 효율적으로 빨리 계산하기 위해 prefix sum을 미리 계산해 두면 됨.


'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N,K,Q,M = map(int, input().split())
    Ks = list(map(int, input().split()))
    Qs = list(map(int, input().split()))
    Ms = []
    for _ in range(M):
        s,e = map(int, input().split())
        Ms.append((s, e))
    return N,Ks,Qs,Ms

def solve(N:int, Ks:list[int], Qs:list[int], Ms:list[tuple[int,int]])->list[str]:
    '''
    Args:
    Returns:
    '''

    # 학생 번호는 3번부터 N+2.
    attn = [0] * (N+3)
    # attn[k]는 학생 번호 k의 출석 여부. 1이면 출석.

    # 졸고 있는 학생 상태 표
    sleep = [0] * (N+3)
    for k in Ks:
        sleep[k] = 1

    # 출석 코드 보내기
    for q in Qs:
        # 코드 받은 학생이 졸고 있으면 모조리 미출.
        if sleep[q]:
            continue
        for qq in range(q, N+3, q):
            if not sleep[qq]: attn[qq] = 1
            # 문제 모호한 부분. 졸고 있는 그 학생 만 미출이고 그 이후는 영향 받지 않음.

    log("----: %s", [3,4,5,6,7,8,9,0,1,2]*((N-3+9)//10))
    log("attn: %s", attn[3:])
    log("slep: %s", sleep[3:])

    # 누적합 계산
    psum = [0]*(N+3)
    # psum[j] 는 처음(학생 3) 부터 학생 j까지의 미출석
    for j in range(3, N+3):
        # j: 학생 번호
        psum[j] = psum[j-1] + (0 if attn[j] else 1)

    log("psum: %s", psum[3:])

    # 검사 구간
    ans = []
    for s,e in Ms:
        ans.append(str(psum[e] - psum[s-1]))

    return ans

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))


'''
예제 입력 1
10 1 3 1
7
3 5 7
3 12
예제 출력 1
4
입장 번호 3번부터 12번까지의 구간에서 입장 번호 4, 8, 11번이 출석 코드를 받지 못했고, 7번은 출석 코드를 받았으나 조느라 출석하지 못했다.

예제 입력 2
50 4 5 1
24 15 27 43
3 4 6 20 25
3 52
예제 출력 2
25

----
pr=20438
run=(python3 a$pr.py)

echo '10 1 3 1\n7\n3 5 7\n3 12' | $run
# 4
echo '50 4 5 1\n24 15 27 43\n3 4 6 20 25\n3 52' | $run
# 25



echo '50 4 5 2\n24 15 27 43\n3 4 6 20 25\n3 25\n26 52' | $run
# 12 13

echo '5 1 1 1\n3\n3\n3 7' | $run
# 5



'''
