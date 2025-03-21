def solve(N:int, graph:list[list]):

    visited = [ 0 for k in range(N*N) ]
    groups = { } # key:group_id, value:number of houses in this group

    def new_group(start:int):
        # find new house group, starting from location 'start'.
        #
        houses = [] # house list.
        # we will track which houses are belonged to this house group

        stack = [ start ]
        in_stack = [ 0 for k in range(N*N) ] # for quick search in stack
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = 1
            houses.append(u)

            # next houses..
            # stack.extend([ x for x in graph[u] if not visited[x] ])
            for x in graph[u]:
                if not visited[x] and not in_stack[x]:
                    stack.append(x)
                    in_stack[x] = 1

        # group id is positive interger. 1, 2, ...
        group_id = len(groups) + 1
        # we just need the number of houses only, not each house list.
        groups[group_id] = len(houses)

        return group_id

    for k in range(N*N):
        if not graph[k]: # no house here
            continue
        if visited[k]:
            continue

        gid = new_group(k)

    result = [ groups[k] for k in groups.keys() ]
    result.sort()
    return result


N = int(input().strip())
A = []
for _ in range(N):
    A.append(input().strip())

# total N**2 nodes, index: 0 ~ N*N-1
graph = [ [] for k in range(N*N) ]

# convert input string to graph
for y in range(N):
    for x in range(N):
        k = y*N + x
        if A[y][x] == '0':
            continue
        graph[k].append(k) # itself

        for (dy,dx) in [ (-1,0), (1,0), (0,-1), (0,1) ]:
            k2 = k + dy*N + dx  # == (y+dy)*N + (x+dx)
            if 0 <= y+dy < N and 0 <= x+dx < N and \
                    A[y+dy][x+dx] == '1' and \
                    k2 not in graph[k]:
                graph[k].append(k2)
        if graph[k]:
            graph[k].sort()

result = solve(N, graph)
print(len(result))
for x in result:
    print(x)
