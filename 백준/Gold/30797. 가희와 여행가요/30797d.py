'''
최소 시간을 달성한 코드.
kruscal 의 disjoint set union 을 재귀 없이 구현하였음!
배워서 활용할 가치가 있음!

https://www.acmicpc.net/source/80832205

80832205 20210805 30797 맞았습니다!!  88012KB   708ms Python 3 1451B
97226408 cafrii   30797 맞았습니다!!  85764KB  1008ms Python 3 1045B

약 30% 정보 더 빠르다!

'''

# region Disjoint Set
class DisjointSet:
    __slots__ = ["parent"]

    def __init__(self, num_node: int):
        self.parent = list(range(num_node))

    def find(self, x: int) -> int:
        parent = self.parent

        stack: list[int] = []
        while parent[x] != x:
            stack.append(x)
            x = parent[x]
        for y in stack:
            parent[y] = x
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.parent[y] = x
        return True


# endregion Disjoint Set

import io, os, sys


def main() -> None:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    num_cities, num_lanes = map(int, input().split())

    lanes: list[tuple[int, int, int, int]] = []
    for _ in range(num_lanes):
        start, end, cost, time = map(int, input().split())
        start -= 1
        end -= 1
        lanes.append((start, end, cost, time))

    lanes.sort(key=lambda x: x[3])
    lanes.sort(key=lambda x: x[2])

    ds = DisjointSet(num_cities)
    num_groups = num_cities
    max_time = 0
    total_cost = 0

    for start, end, cost, time in lanes:
        if ds.union(start, end):
            num_groups -= 1
            max_time = max(max_time, time)
            total_cost += cost

    if num_groups == 1:
        print(max_time, total_cost)
    else:
        print(-1)


sys.exit(main())

