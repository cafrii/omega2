
def solve(A:list[int], M:int):
    '''
    generator that yield answer line by line.
    '''
    A = list(set(A))
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
