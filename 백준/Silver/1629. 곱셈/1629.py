'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

참고
https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation

임의의 B에서 A^B mod C를 빨리 계산하는 방법

예: (5 ^ 117) mode 19

1단계: 이진수를 이용하여 B를 2의 거듭제곱으로 분해합니다.
    117 = 1110101b
        = 2^0 + 2^2 + 2^4 + 2^5 + 2^6
        = 1 + 4 + 16 + 32 + 64

2단계: 2 의 거듭제곱의 mod C 를 계산합니다
5^1 mod 19 = 5
5^2 mod 19 = (5 * 5) mod 19 = 25 mod 19 = 6
5^4 mod 19 = (5^2 * 5^2) mod 19 = (5^2 mod 19 * 5^2 mod 19) mod 19 = (6 * 6) mod 19 = 17
5^8 mod 19 = (5^4 * 5^4) mod 19 = ... = (17 * 17) mod 19 = 4
5^16 mod 19 = (5^8 * 5^8) mod 19 = ... = (4 * 4) mod 19 = 16
5^32 mod 19 = 9
5^64 mod 19 = 5

3단계: 계산된 mod C 값을 결합하기 위한 모듈러 곱셈 성질 이용
5^117 mod 19 = ( 5^1 * 5^4 * 5^16 * 5^32 * 5^64) mod 19
5^117 mod 19 = ( 5^1 mod 19 * 5^4 mod 19 * 5^16 mod 19 * 5^32 mod 19 * 5^64 mod 19) mod 19
5^117 mod 19 = ( 5 * 17 * 16 * 9 * 5 ) mod 19
5^117 mod 19 = 61200 mod 19 = 1
5^117 mod 19 = 1


'''

A,B,C = map(int, input().split())

# calculate A**B mod C

# step 1:
# get binary representation of B
br = bin(B)[2:][::-1] # remove prefix '0b', reverse bits
# br[k] 는 2^k 항의 계수

# step 2:
# (A의 (2 의 거듭제곱)의 거듭제곱) 의 mod C 를 계산
# A^1 mod C = ms0
# A^2 mod C = (A^1 * A^1) mod C = (A^1 mod C * A^1 mod C) mod C = (ms0 * ms0) mod C = ms1
# A^4 mod C = (A^2 * A^2) mod C = (A^2 mod C * A^2 mod C) mod C = (ms1 * ms1) mod C = ms2
# A^8 mod C = (A^4 * A^4) mod C = ... = (ms2 * ms2) mod C = ms3
# A^16 mod C = (A^8 * A^8) mod C = ... = (ms3 * ms3) mod C = ms4
# A^32 mod C = ms5
# A^64 mod C = ms6
# ...

ms = [ A % C ]    # ms[0] = A^1 mod C
for k in range(1, len(br)):
    ms.append( (ms[-1]*ms[-1]) % C )

# step 3:
# 계산된 mod C 값을 결합하기 위한 모듈러 곱셈 성질 이용
# 예를 들어 B 가 117 (1110101b) 라면 br 은 "1010111"
#         B = 1 + 4 + 16 + 32 + 64
# A^117 mod C
#   = ( A^1 * A^4 * A^16 * A^32 * A^64) mod C
#   = ( A^1 mod C * A^4 mod C * A^16 mod C * A^32 mod C * A^64 mod C) mod C
#   = ( 5 * 17 * 16 * 9 * 5 ) mod C  # 괄호 안의 곱셈도 overflow 될 수 있으니 각 단계 별로 모두 mod 적용
#   = ((((( 5 * 17 mod C) * 16 mod C) *9 mod C) *5 mod C)
#   = 1


ans = 1
for k in range(len(br)):
    if br[k] == '1':
        ans = (ans * ms[k]) % C

print(ans)

'''
예제 입력 1
10 11 12
예제 출력 1
4

echo '2147483647 2147483647 2147483647' | python3 1629.py
-> 0


echo '1234567 1234567 12344321' | python3 1629.py
-> 5205370


echo '3 2147483647 8' | python3 1629.py
-> 3


echo '14 1 10' | python3 1629.py
-> 4


echo '2147483647 2147483647 2147483646' | python3 1629.py
-> 1


echo '5 111 50888' | python3 1629.py
-> 16437


echo '6 11 13' | python3 1629.py
-> 11


echo '4 1 2' | python3 1629.py
-> 0


echo '99999 99999 100000' | python3 1629.py
-> 99999


echo '0 1 1' | python3 1629.py
-> 0


echo '2147483647 2147483647 100001' | python3 1629.py
-> 7569


echo '5 1 2' | python3 1629.py
-> 1

'''





