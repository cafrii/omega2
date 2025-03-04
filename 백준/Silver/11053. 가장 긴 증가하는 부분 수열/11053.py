'''
가장 긴 증가하는 부분 수열 성공
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	189422	76775	50939	38.375%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

'''

# 이 함수는 디버깅용.
def maxlenstr(a:list):
    return ','.join([ f"{i}:{x}" for i,x in enumerate(a) if x > 0 ])

def solve(nums:list):
    # max_len = {}
    # max_len[num] 은 최종 숫자 num 으로 끝나는 가장 긴 부분 수열의 길이.

    max_n = max(nums)
    max_len = [ 0 ] * (max_n + 1)

    for n in nums:
        # n 이 이전 부분 수열의 뒤에 붙을 수 있는 경우는 끝 수가 n 보다 작아야 함.
        # n-1 까지 중 최대 길이를 찾고
        # 그 길이에 +1 한 것이 이번 step 에서의 최대 길이

        new_max = max(max_len[i] for i in range(n)) + 1

        if new_max > max_len[n]:
            max_len[n] = new_max
            # print(f"+{n} -> {maxlenstr(max_len)}")
        # else:
        #     print(f"+{n}")

    return max(max_len)


N = int(input().strip())
A = list(map(int, input().split()))
print(solve(A))


'''
10 20 10 30 20 50
10:1
10:1 20:2
10:1 20:2 30:3
10:1 20:2 30:3 50:4
+11
10:1 11:2 20...
+12


예제 입력 1
6
10 20 10 30 20 50

예제 출력 1
4


12
10 20 10 30 20 50 15 11 12 13 14 15


'''
