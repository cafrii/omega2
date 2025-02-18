
N = int(input())
words = []
for _ in range(N):
    words.append(input())

# remove duplicates
words = list(set(words))

# sorty by length and then by lexicographical order
words.sort(key=lambda a: (len(a), a))

for word in words:
    print(word)
    