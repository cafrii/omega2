
import sys
input = sys.stdin.readline

bt = [0] # binary tree

N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(bt) < 2:
            print(0)
            continue

        print(bt[1]) # print max
        bt[1] = bt[-1]
        bt.pop()

        # and re-balance tree
        k = 1
        while 2*k < len(bt): # 최소한 하나의 자식은 존재하는 동안은 반복
            if len(bt) <= 2*k+1: # 두 자식은 아닌 경우. 즉 단일 자식
                if bt[k] < bt[2*k]: # 자식이 더 크면 교환
                    bt[k], bt[2*k] = bt[2*k], bt[k]
                break # 더 이상의 자식은 없으니 종료.

            # 두 자식 중 더 큰 자식을 선택
            bigger = 2*k if bt[2*k] > bt[2*k+1] else 2*k+1
            if bt[k] < bt[bigger]: # 큰 자식이 본인보다 더 크면 교환
                bt[k], bt[bigger] = bt[bigger], bt[k]
                k = bigger
            else: # 본인이 자식보다 더 크면 리밸런싱 종료
                break
        #print(bt, file=sys.stderr)
    else:
        bt.append(x) # 새 값을 맨 아래에 추가하고
        k = len(bt) - 1
        # 리밸런싱
        while k > 1:
            if bt[k] <= bt[k//2]: # 자식인 내가 부모보다 더 크지 않다면 종료
                break
            bt[k], bt[k//2] = bt[k//2], bt[k]
            k //= 2
        #print(bt, file=sys.stderr)
