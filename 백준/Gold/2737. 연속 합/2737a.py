'''
clean 버전. (제출용)

'''


import sys
input = sys.stdin.readline

def solve(N):
    cnt = 0
    # sl: sequence length
    for sl in range(2, N+1):
        if sl % 2 == 0:
            lcenter = N // sl  # lower center
            if lcenter - sl//2 + 1 < 1:
                break
            # sl 이 짝수이면 N/sl 은 *.5 형태가 되어야 함.
            if 2*N % sl != 0 or N%sl == 0:
                continue
            # 예: N==14, sl==4, N/sl = 3.5, lcenter = 3
            # seq:  2 3 (3.5) 4 5
            cnt += 1

        else:
            # sl 이 홀수이면 N은 sl로 나누어 떨어지는 수 이어야 함.
            if N % sl != 0:
                continue

            center = N // sl
            # center 를 중심으로 양쪽에 sl//2 개 씩의 숫자가 붙어야 함.
            if center - sl//2 < 1:
                break
            # 예: N=15, sl=5, center = 15/5 = 3
            # seq:  1 2 3 4 5
            cnt += 1

    return cnt


T = int(input().strip())
for k in range(T):
    n = int(input().strip())
    print(solve(n))



'''
run=(time python3 2737a.py)

echo '7\n6\n9\n8\n1800\n987654321\n987654323\n987654325' | $run

echo '15\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15' | $run
->        0  0  1  0  1  1  1  0  2  1   1   1   1   1   3

'''
