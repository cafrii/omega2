'''
15988번

합격률이 낮길래 어려운 문제인가 싶었는데, 그냥 지저분한 문제일 뿐이다.

동일 코드를 Python3 대신 PyPy3 로 하면 통과 됨.
내 알고리즘에는 전혀 문제가 없지만 단순히 python 이라는 이유 만으로 시간 초과가 되게끔 설정되어 있음.

문제 조건에 T 자체에 제한을 두지 않았으니,
기존에 통과 한 코드도 T를 조금 늘림으로써 또 FAIL 되게도 만들 수 있고..

1, 2, 3 더하기 3

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	39656	14563	11233	34.835%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
n은 양수이며 1,000,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
'''


N_MAX = 1_000_000
R_MOD = 1_000_000_009 # mod value for the result

# 항상 그렇듯이, 이 greedy 버전은 자체 검증 용도이다.
# N이 27~ 를 넘어가면 느려지는 듯. 호출 깊이도 문제가 될 수 있다.
def solve_greedy(N:int):

    if N <= 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2 # 1+1, 2
    if N == 3:
        return 4 # (1+1)+1, (2)+1, (1)+2, 3
        # 문제 정의에 의해서, 1+2 와 2+1 을 각각의 경우로 카운트 하고 있음.
        # 이는 A[2]의 경우의 수에 +1, A[1]의 경우의 수에 +2 를 한 것임.
    return (solve_greedy(N-1) + solve_greedy(N-2) + solve_greedy(N-3)) % R_MOD


# 최대로 N_MAX+1 크기가 필요하지만, max(N)을 알아낸 후 초기화 하도록 하자.
A = []

# 어디까지의 답이 현재 계산되고 저장되었는지.
# num_answer 가 100 이면 A[100] 까지는 유효함.
num_answer = 0


def solve(N:int):
    # assume 0 < N <= N_MAX
    '''
    주어진 수 N 에 대한 답 A[N]을 찾기 위해서, A[N-1], A[N-2] 등을 이용하면 됨.
    A의 크기는 필요한 만큼 초기화 되어 있음.
    A[num_answer] 까지는 답이 구해져 있는 상태.
    '''
    global A, num_answer

    if num_answer < 5:
        A[0] = 0
        A[1] = 1 # 1
        A[2] = 2 # 2, (1)+1
        A[3] = 4 # 3, (2)+1, (1+1)+1, (1)+2
        A[4] = 7 # A[3], A[2], A[1] -> 7
        A[5] = 13 # 7+4+2
    num_answer = 5

    if N > num_answer:
        # 아직 채워지지 않은 정답을 지금 채운다.
        for k in range(num_answer, N+1):
            A[k] = (A[k-1] + A[k-2] + A[k-3]) % R_MOD
        num_answer = N

    return A[N]


T = int(input().strip())
Ns = [0] * T

for k in range(T):
    Ns[k] = int(input().strip())
n_max = max(Ns)
A = [0] * (n_max+1)


for n in Ns:
    print(solve(n))
    # print(solve_greedy(n))


'''
예제 입력 1
3
4
7
10

예제 출력 1
7
44
274

시간 제한
echo "1\n1000000" | time python3 a.py
810017797
python3 a.py  0.15s user 0.02s system 98% cpu 0.166 total

'''