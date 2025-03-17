
N_MAX = 1_000_000
R_MOD = 1_000_000_009 # mod value for the result

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
