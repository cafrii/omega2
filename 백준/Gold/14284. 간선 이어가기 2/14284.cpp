/*
c++ 연습용

11:42~12:00

*/


#include <iostream>
#include <vector>
#include <queue> // priority_queue

using namespace std;
using GRAPH = vector<vector<tuple<int,int>>>;
    // nodes, links, (end_node, link_cost)

static const int INF = 1e8;

// node number starts from 0.
int dijkstra(const GRAPH& graph, int start, int end)
{
    int n = (int)graph.size();

    vector<int> mincost(n, INF);
    priority_queue<tuple<int,int>> que; // max que.

    que.push({0, start});

    while (!que.empty()) {
        auto [cost, now] = que.top();
        que.pop();
        cost = -cost;

        if (now == end) return cost;
        if (mincost[now] < cost)
            continue;

        for (auto [nxt, lc]: graph[now]) {
            if (cost+lc >= mincost[nxt])
                continue;
            que.push({-(cost+lc), nxt});
            mincost[nxt] = cost+lc;
        }
    }
    return -1;
}



int main()
{
    int n, m, a, b, c, s, t;
    scanf("%d%d", &n, &m);

    // GRAPH graph(n, vector<tuple<int,int>>{});
    GRAPH graph(n);

    for (int i=0; i<m; i++) {
        scanf("%d%d%d", &a, &b, &c);
        graph[a-1].push_back({b-1, c});
        graph[b-1].push_back({a-1, c});
    }
    scanf("%d%d", &s, &t);

    printf("%d\n", dijkstra(graph, s-1, t-1));
    return 0;
}


/*
clang++ -std=c++20 -o out/a 14284.cpp

run=out/a

echo '8 9\n1 2 3\n1 3 2\n1 4 4\n2 5 2\n3 6 1\n4 7 3\n5 8 6\n6 8 2\n7 8 7\n1 8' | $run
-> 5



*/