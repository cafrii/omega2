'''
벌집
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	203881	92905	78962	44.998%
문제


위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

예제 입력 1
13
예제 출력 1
3

범위 -> 링 레벨 (도달 거리))
1 -> 1
2~7 -> 2
8~19 -> 3
20~37 -> 4

주어진 레벨 L 의 범위 중 큰 값을 f(L) 이라고 하면
f(0) = 1 # assume
f(1) = 1 = f(0) + 6*0
f(2) = 7 = f(1) + 6 = f(1) + 6*1
f(3) = 19 = f(2) + 12 = f(2) + 6*2
...
f(L) = f(L-1) + 6*(L-1)

f(L) = 6*(L-1) + 6*(L-2) + .. + 6*1 + f(1)


--- below code cause memory overflows. we cannot use list.

MAX_N = 1_000_000_000

N = int(input().strip())
m6 = [ 0 ] # multiple of six
f_end = [ 1 ] # f(0)=1

for level in range(1,MAX_N):
    fmax_next = f_end[level-1] + m6[level-1]
    f_end.append(fmax_next)
    m6.append(m6[level-1] + 6)
    # print(f'Level {level}: {f_end[level-1]+1} ~ {f_end[level]},  m6[{level-1}] = {m6[level-1]}')
    if f_end[level-1] < N <= f_end[level]:
        print(level)
        break

'''

MAX_N = 1_000_000_000

N = int(input().strip())
m6 = 0
f_prev = 1

for L in range(1,MAX_N):
    f_next = f_prev + m6
    # print(f'Level {L}: {f_prev+1} ~ {f_next},  m6 = {m6}')
    if N <= f_next:
        print(L)
        break
    f_prev = f_next
    m6 += 6
