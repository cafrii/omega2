/*
    c++ 로 재구현 연습.

*/

#include <iostream>
#include <algorithm>
#include <set>

#include "../../pycpp/src/types/pyc_tostring.hpp"


using namespace std;
namespace pyc = com::cafrii::pyc;


void mark_region(const vector<vector<int>>& grid, int lvl, vector<vector<int>>& region, int r, int c, int rid)
{
    int n = (int)grid.size();

    using point = tuple<int,int>;

    vector<point> stack;
    stack.push_back(point{r, c});

    auto delta = vector<tuple<int,int>> {{0,1}, {0,-1}, {1,0}, {-1,0}};

    while (!stack.empty()) {
        auto [cr, cc] = stack.back();
        stack.pop_back();

        for (auto [dr,dc]: delta) {
            int nr = cr+dr, nc = cc+dc;
            if (!(0 <= nr && nr < n && 0 <= nc && nc < n)) continue;
            if (grid[nr][nc] <= lvl) continue;
            if (region[nr][nc] >= 0) continue;

            stack.push_back(point{nr, nc});
            region[nr][nc] = rid;
        }
    }
    return;
}


int count_region(const vector<vector<int>>& grid, int lvl)
{
    int n = (int)grid.size();
    vector<vector<int>> region(n, vector<int>(n, -1));
    int num_region = 0;

    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            if (grid[r][c] <= lvl) continue;
            if (region[r][c] >= 0) continue;

            mark_region(grid, lvl, region, r, c, num_region);
            num_region ++;
        }
    }
    // printf("level: %d, num region: %d\n%s\n", lvl, num_region, pyc::to_string(region).c_str());
    return num_region;
}

int solve(const vector<vector<int>>& grid)
{
    int n = (int)grid.size();

    set<int> levels;
    for (auto& r: grid)
        for (auto& c: r)
            levels.insert(c);
    // printf("%s\n", pyc::to_string(levels).c_str());

    vector<int> counts {1}; // 1: a whole grid
    for (auto lvl: levels) {
        int c = count_region(grid, lvl);
        if (c <= 0) break; // all cells are not safe. stop loop.
        counts.push_back(c);
    }

    auto maxit = max_element(counts.begin(), counts.end());
    return *maxit;
}


int main()
{
    int n;
    scanf("%d", &n);
    vector<vector<int>> grid(n);

    for (int i=0; i<n; i++) {
        grid[i] = vector<int>(n);
        for (int j=0; j<n; j++)
            scanf("%d", &grid[i][j]);
    }

    printf("%d\n", solve(grid));
    return 0;
}


/*
clang++ -std=c++20 -o out/a 2468.cpp

run=out/a

echo '5\n6 8 2 6 2\n3 2 3 4 6\n6 7 3 3 2\n7 2 5 3 6\n8 9 5 2 7' | $run
-> 5

echo '7\n9 9 9 9 9 9 9\n9 2 1 2 1 2 9\n9 1 8 7 8 1 9\n9 2 7 9 7 2 9\n9 1 8 7 8 1 9\n9 2 1 2 1 2 9\n9 9 9 9 9 9 9' | $run
-> 6

*/
