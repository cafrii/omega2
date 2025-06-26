/*
    14938
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <numeric> // accumulate

// #include "../../pycpp/src/types/pyc_tostring.hpp"
// namespace pyc = com::cafrii::pyc;

using namespace std;

vector<vector<tuple<int,int>>> graph;
// graph[node] = { (node1,dist1), (node2,dist2), ... }

const int INF = 9999;

#define log(fmt, ...) ({ fprintf(stderr, fmt, ##__VA_ARGS__); fflush(stderr); })


/*
    stop searching if total distance exceed m.
    return node number list of interes.
*/
vector<int> dijkstra(int start, int num_nodes, int m)
{
    priority_queue<tuple<int,int>> pq;
    // element: (dist, node)
    // priority que works as maximum que by default.

    vector<int> mindist(num_nodes, INF);

    // dist is saved with "negative" sign, which makes effect of minimum que.
    pq.push({-0, start});
    mindist[start] = 0; // also works as 'visited' mask.

    while (!pq.empty()) {
        auto [dist, cur] = pq.top();
        pq.pop();
        dist = -dist; // total distance from start
        // log("[dist %d] node %d\n", dist, cur);

        if (dist > m) // stop looping
            break;
        if (mindist[cur] < dist) // shorter path already visited here
            continue;

        for (auto [nxt, lc]: graph[cur]) {
            // log("  next %d, lc %d\n", nxt, lc);
            if (mindist[nxt] < dist + lc) continue; // 더 짧은 경로로 이미 방문.
            if (dist + lc > m) continue; // early exit
            // log("    push %d, dist %d\n", nxt, dist+lc);
            mindist[nxt] = min(mindist[nxt], (dist+lc));
            pq.push({-(dist+lc), nxt});
        }
    }
    // 반경 m 이내의 노드 번호만 추출하여 리턴. 순서 중요하지 않음.
    vector<int> noi; // nodes of interest
    for (int i=0; i<num_nodes; i++) {
        if (mindist[i] < INF)
            noi.push_back(i);
    }
    return noi;
}


int main()
{
    int n, m, r;
    int a, b, d;
    scanf("%d%d%d", &n, &m, &r);

    vector<int> items(n);
    for (int i=0; i<n; i++)
        scanf("%d", &items[i]);

    graph.resize(n);
    for (int i=0; i<r; i++) {
        scanf("%d%d%d", &a, &b, &d);
        graph[a-1].push_back({b-1, d});
        graph[b-1].push_back({a-1, d});
    }

    auto scores = vector<int>(n, 0);
    for (int i=0; i<n; i++) {
        // log("----------- dijkstra from node %d \n", i);
        // get accessible node list
        auto nodes = dijkstra(i, n, m);

        // calculate score sum
        // int count = 0;
        // for (auto k: nodes)
        //     count += items[k];
        // scores[i] = count;
        scores[i] = accumulate(nodes.begin(), nodes.end(), 0,
                [&items](int sum, int k){ return sum + items[k]; });
    }
    auto it = max_element(scores.begin(), scores.end());
    printf("%d\n", *it);
    return 0;
}



/*
clang++ -std=c++20 -Wall -o out/a 14938.cpp
run=out/a

echo '5 5 4\n5 7 8 2 3\n1 4 5\n5 2 4\n3 2 3\n1 2 3' | $run


*/

