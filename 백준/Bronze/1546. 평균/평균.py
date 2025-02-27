N = int(input())
A = list(map(int, input().split()))

M = max(A)
B = list(map(lambda x: x/M*100, A))
print(sum(B)/len(B))
