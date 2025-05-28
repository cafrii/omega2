'''

다른 해법
https://www.acmicpc.net/source/94810271

앞에서부터 순서대로 처리하는데
- 가 한번이라도 출현한 이후의 +는 모두 적절한 괄호를 이용하여 -처럼 동작시킬 수 있다는 점을 활용.

'''


math = input()
m = 1
fer = ""
last = 0
for i in math:
    if i == "+":
        last += int(fer) * m
        print(f"+ fer:{fer}, m:{m} -> last:{last}")
        fer = ""
    elif i == "-":
        last += int(fer) * m
        print(f"- fer:{fer}, m:{m} -> last:{last}")
        fer = ""
        m = -1
    else:
        fer += i
        print(f"  fer:{fer}")

print(f"==> final: last:{last} fer:{fer} m:{m}")
print(last + int(fer) * m)

