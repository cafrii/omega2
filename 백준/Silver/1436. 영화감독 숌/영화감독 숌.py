def solve(N:int)->int:
    num_matches = 0
    for n in range(int(1e9)):
        # n 의 범위 끝은 충분히 커야 한다.
        if '666' in str(n):
            num_matches += 1
            if num_matches == N:
                return n
    return 0 # 못찾아서 실패. 이런 경우는 발생하지 않음.


N = int(input().strip())
print(solve(N))
