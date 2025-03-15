
MAX_N = 100_000

'''
메모리 제한이 있으므로, A를 미리 받아서 저장하지 않고 입력 받으면서 계산한다.
'''
def solve(N:int):
    # 각 step 단계에서:
    #  smax[k]: k 위치에서 마지막으로 끝난 경우 최대 스코어. (k=0 or 1 or 2)
    #  smin[k]: k 위치에서 마지막으로 끝난 경우 최소 스코어.
    #
    # 첫번째 단계는 그냥 입력 값 그 자체.
    smax = list(map(int, input().strip().split()))
    smin = smax.copy()

    for k in range(1, N):
        a0, a1, a2 = map(int, input().strip().split())
        
        # update max
        smax = [
            max(smax[0], smax[1]) + a0,
                # 0 위치에서 끝나려면 이전 단계의 0, 또는 1 에서 끝나야 함.
            max(smax) + a1,
                # 1 위치는 이전 단계 어디에서든 올 수 있음.
            max(smax[1], smax[2]) + a2,
        ]
        # update min
        smin = [
            min(smin[0], smin[1]) + a0,
            min(smin) + a1,
            min(smin[1], smin[2]) + a2,
        ]
    return max(smax), min(smin)

def main1():
    N = int(input().strip())
    m1,m2 = solve(N)
    print(m1,m2)

main1()

