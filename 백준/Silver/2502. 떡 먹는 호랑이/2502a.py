'''
또 다른 풀이법

https://www.acmicpc.net/source/94276420

예시로 풀어보면 이해가 된다.

예: D,K = 7,31

내 방식이라면 C는 다음과 같음.
(1,0) (0,1) (1,1) (1,2) (2,3) (3,5) (5,8)

그런데 가만히 살펴보면..
- C[1] 이 곧 fifo 수열과 거의 유사하다! 0 1 1 2 3 5 8
- C[0] 또한 뒷 부분이 fifo 수열이다!   1 0 1 1 2 3 5

그래서 그냥 fifo 수열을 구한 후 거기에서 두 계수 ca, cb 를 얻어내고 있음.

              d
3 2 5 7 12 19 31
1 1 2 3  5  8 13  # fifo

'''


d, k = map(int, input().split())

fibo = [0] * (d+1)
fibo[1] = 1
fibo[2] = 1

for i in range(3, d+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

A = fibo[d - 2]
B = fibo[d -1]

for x in range(1, k+1):
    if(k - A * x) % B == 0:
        y = (k - A * x) // B
        if y >= 1:
            print(x)
            print(y)
            break

