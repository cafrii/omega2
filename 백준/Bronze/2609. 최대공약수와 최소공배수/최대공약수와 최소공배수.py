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
