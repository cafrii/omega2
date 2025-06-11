'''
15666번

N과 M (12) 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	26308	20718	17871	79.388%

문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
- 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

--------

10:57~11:12


'''


def solve(A:list[int], M:int):
    '''
    generator that yield answer line by line.
    '''
    A = list(set(A)) # remove redundancy
    A.sort()
    digits = [0]*M  # target number array to make

    def fill(pos, min_digit):
        # pos is the index of array 'digits' where we should fill in this step.
        # any number of list A, which is not-less than min_digit, can be used to fill.
        # this function is also generator function.
        if pos == M:
            yield ' '.join(map(str, digits))
            return
        for a in A:
            if a < min_digit: continue
            digits[pos] = a # fill one digit
            yield from fill(pos+1, a)

    yield from fill(0, 0)


N,M = map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == N

gen_answer = solve(A, M)
for ln in gen_answer:
    print(ln)



'''
run=(python3 15666.py)

예제 입력 1
3 1
4 4 2
예제 출력 1
2
4

echo '3 1\n4 4 2' | $run


예제 입력 2
4 2
9 7 9 1
예제 출력 2
1 1
1 7
1 9
7 7
7 9
9 9

예제 입력 3
4 4
1 1 2 2
예제 출력 3
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2



echo '4 4\n1 1 2 2' | $run


'''
