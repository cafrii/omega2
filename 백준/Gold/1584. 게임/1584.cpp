/*


*/


#include <queue>


using namespace std;

using Elem = std::tuple<int,int,int>;
// 순서대로 cost, y, x

const int SZ = 501;
const int GOAL = 500;

const int INF = (SZ * SZ) + 1;
// const int INF = INT32_MAX;

int solve(vector<vector<int>>& board)
{
    // min costs table, 2-d vector.
    auto min_cost = vector<vector<int>>(SZ, vector<int>(SZ, INF));

    // priority_queue<Elem> pq;
    // 주의! c++ stl 의 pq 는 max que 로 동작한다!
    // 최소 큐로 동작 시키려면 기본 less 대신 greater를 사용해야 함.
    priority_queue<Elem, vector<Elem>, greater<Elem>> pq;


    pq.push(Elem(0, 0, 0));
    min_cost[0][0] = 0;

    std::vector<std::array<int,2>> delta = { {1,0}, {-1,0}, {0,1}, {0,-1} };

    for (; !pq.empty(); ) {
        // since c++17
        auto [cost, y, x] = pq.top();
        pq.pop();

        if (y == GOAL && x == GOAL)
            return min_cost[y][x];

        if (min_cost[y][x] < cost)
            continue;

        for (auto& d: delta) {
            auto ny = y+d[0], nx = x+d[1];

            if (min(nx,ny) < 0 || max(nx,ny) > GOAL)
                continue;

            if (board[ny][nx] == 2)
                continue;

            auto next_cost = (board[ny][nx]==1) ? cost+1 : cost;
            // 이미 방문했던 지점인 경우, 더 나아지지 않았다면 재방문 의미 없음.
            if (next_cost >= min_cost[ny][nx])
                continue;

            pq.push(Elem(next_cost, ny, nx));
            min_cost[ny][nx] = next_cost;
        }
    }
    return -1;
}

#include <iostream>

void fill_region(vector<vector<int>>& board, int y1, int x1, int y2, int x2, int mark)
{
    if (y1 > y2) swap(y1, y2);
    if (x1 > x2) swap(x1, x2);

    for (auto y=y1; y<=y2; y++) {
        // use std::fill
        fill(board[y].begin()+x1, board[y].begin()+x2+1, mark);
        // for (auto x=x1; x<=x2; x++)
        //     board[y][x] = mark;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    auto board = vector<vector<int>>(SZ+1, vector<int>(SZ+1, 0));

    int n, m;
    int x1, y1, x2, y2;

    cin >> n;  // num risky region
    for (auto i=0; i<n; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        fill_region(board, y1, x1, y2, x2, 1);
    }

    cin >> m;  // num dead region
    for (auto i=0; i<m; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        fill_region(board, y1, x1, y2, x2, 2);
    }

    cout << solve(board) << endl;
    return 0;
}

/*
clang++ -std=c++17 -o 1584 1584.cpp


run=(./1584)

echo '1\n500 0 0 500\n1\n0 0 0 0' | $run
echo '0\n0' | $run
echo '2\n0 0 250 250\n250 250 500 500\n2\n0 251 249 500\n251 0 500 249' | $run
echo '2\n0 0 250 250\n250 250 500 500\n2\n0 250 250 500\n250 0 500 250' | $run

->
1000
0
1000
-1

*/
