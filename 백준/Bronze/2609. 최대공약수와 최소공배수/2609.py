'''
2609번

최대공약수와 최소공배수 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	134335	77698	63317	57.667%

문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''

def get_divs(n:int) -> set:
    divs = set()
    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            divs.update((i, n//i))
    # return sorted(list(divs))
    return divs

def gcd(a, b):
    divs = get_divs(a) & get_divs(b)
    return sorted(list(divs))[-1]

def lcm(a, b):
    return abs(a * b)//gcd(a, b)

A,B = map(int, input().split())
print(gcd(A,B), lcm(A,B), sep='\n')

'''
예제 입력 1
24 18

예제 출력 1
6
72
'''