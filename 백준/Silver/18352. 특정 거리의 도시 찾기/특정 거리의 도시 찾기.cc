
#include <iostream>
#include <algorithm>
#include <map>
#include <deque>
#include <sstream>


using namespace std;

/*
    custom graph type.
    key: start node
    value: end node list as vector<int>
*/
using Map = map<int,vector<int>>;

vector<int> solve(Map& map, int N, int K, int X)
{
    auto que = deque<int>();
    auto mindist = vector<int>(N+1, -1); // [0] is not used.
    vector<int> answer;

    // now, start from node X.
    que.push_back(X);
    mindist[X] = 0;

    int cur; // visiting node
    int dist; // distance up to here

    while (!que.empty()) {
        cur = que.at(0);
        dist = mindist[cur];
        que.pop_front();

        if (dist == K) {
            answer.push_back(cur);
            continue; // no need to consider next node.
        }
        if (dist > K) // no more need to continue.
            break;
        if (!map.contains(cur)) // map does not have node-cur.
            continue;
        for (auto nxt: map[cur]) {
            if (mindist[nxt] >= 0)
                continue;
            que.push_back(nxt);
            mindist[nxt] = dist + 1;
        }
    }
    if (answer.empty())
        answer.push_back(-1);

    sort(answer.begin(), answer.end());
    return answer;
}


int main()
{
    int N, M, K, X, A, B;
    scanf("%d%d%d%d", &N, &M, &K, &X);

    auto graph = Map();
    for (int i=0; i<M; i++) {
        scanf("%d%d", &A, &B);
        graph[A].push_back(B);
    }
    auto ans = solve(graph, N, K, X);
    for (auto val: ans)
        printf("%d\n", val);
    return 0;
}
