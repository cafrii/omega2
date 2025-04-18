

while True:
    s = input().strip()
    # is input string '010' is allowed? it can be. so, remove leading 0s.
    s = str(int(s))
    if s == '0':
        break
    print('yes' if s == s[::-1] else 'no')


def is_palin(s:str):
    # exercise which not use slice
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

