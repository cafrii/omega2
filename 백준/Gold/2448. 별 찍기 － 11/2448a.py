'''
다른 풀이.
우측 시프트 방식으로 하면 더 간단한 듯.

https://www.acmicpc.net/source/95758548

'''

def triangle(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    else:
        upper = triangle(n // 2)
        lower = []
        width = n // 2
        result = []
        for line in upper:
            result.append(" " * width + line + " " * width)
        for line in upper:
            result.append(line + " " + line)
        return result

print('\n'.join(triangle(int(input()))))

