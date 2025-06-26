
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <numeric> // accumulate

using namespace std;

vector<vector<tuple<int,int>>> graph;
// graph[node] = { (node1,dist1), (node2,dist2), ... }

const int INF = 9999;

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

        if (dist > m) // stop looping
            break;
        if (mindist[cur] < dist) // shorter path already visited here
            continue;

        for (auto [nxt, lc]: graph[cur]) {
            if (mindist[nxt] < dist + lc) continue; // 더 짧은 경로로 이미 방문.
            if (dist + lc > m) continue; // early exit
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
    int n, m, r, t;
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
        // get accessible node list
        auto nodes = dijkstra(i, n, m);
        // calculate score sum
        scores[i] = accumulate(nodes.begin(), nodes.end(), 0,
                [&items](int sum, int k){ return sum + items[k]; });
    }
    auto it = max_element(scores.begin(), scores.end());
    printf("%d\n", *it);
    return 0;
}
