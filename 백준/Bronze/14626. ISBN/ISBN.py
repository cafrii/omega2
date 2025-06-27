
def is_valid_isbn(arr:list[int])->bool:
    assert len(arr) == 13
    m = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    return sum(a*b for a,b in zip(arr,m)) % 10 == 0

line = input().strip()
assert len(line) == 13
arr = []
index = -1
for i,c in enumerate(line):
    if c == '*':
        index,c = i,'0'
    arr.append(int(c))
assert 0 <= index < 13

for k in range(0,10):
    arr[index] = k
    if is_valid_isbn(arr):
        print(k)
