
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