#include <cstdio>
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

struct Edge {
    int u, v, c; // c: cost of u-v edge
};
using Roots = vector<int>;

int find_root(int a, Roots& roots)
{
    if (a == roots[a]) return a;
    roots[a] = find_root(roots[a], roots);
    return roots[a];
};

int solve(int n, int t, deque<Edge>& edges)
{
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b){ return a.c < b.c; });

    Roots roots(n+1);  // roots[0] is not used.
    for (int k=0; k<n+1; k++) roots[k] = k;

    int num_edges = 0;
    int extra_cost = 0;
    int total_cost = 0;

    while (!edges.empty()) {
        auto [a, b, c] = edges[0];
        edges.pop_front();
        int ra = find_root(a, roots);
        int rb = find_root(b, roots);
        if (ra == rb) continue;
        roots[b] = roots[rb] = ra;
        num_edges++;
        total_cost += (c + extra_cost);
        extra_cost += t;
        if (num_edges >= n-1)
            break;
    }
    return total_cost;
}

int main()
{
    int n, m, t, a, b, c;
    scanf("%d%d%d", &n, &m, &t);
    deque<Edge> edges;
    for (int i=0; i<m; i++) {
        scanf("%d%d%d", &a, &b, &c);
        edges.push_back({a, b, c});
    }
    printf("%d\n", solve(n, t, edges));
    return 0;
}
