/*
    impl. with c++

*/

#include <iostream>
#include <queue>
#include <algorithm>
#include <sstream>

using namespace std;

int Solve(const vector<pair<int,int>>& tbl)
{
    priority_queue<int> pq; // max que

    pq.push(-tbl[0].second); // use with sign inversion
    for (int k=1; k<(int)tbl.size(); k++) {
        auto& t = tbl[k];
        if (-pq.top() <= t.first)
            pq.pop();
        pq.push(-t.second);
    }
    return (int)pq.size();
}

int main()
{
    int n;
    scanf("%d", &n);
    vector<pair<int,int>> tbl(n);
    for (auto i=0; i<n; i++) {
        scanf("%d%d", &tbl[i].first, &tbl[i].second);
    }
    sort(tbl.begin(), tbl.end());
    printf("%d\n", Solve(tbl));
    return 0;
}


/*
clang++ -std=c++17 -o out/a 11000.cpp

run=out/a
echo '3\n1 3\n2 4\n3 5' | $run
-> 2

export _N=200
export _N=200000

(python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
N = int(os.getenv('_N','10')) # 2000 #200_0000
print(N)
for k in range(N):
    print(0, randint(1,int(1e9)))
EOF
) | time $run

->
0.41s user 0.00s system 95% cpu 0.436 total

// 어떤 이유인지 몰라도 c++ 이 python 보다 더 느리다???
// cin/cout 대신 scanf/printf 로 변경 후 속도 개선되었음.
// 문제 출제 스크립트의 속도가 병목임.
->
0.19s user 0.01s system 74% cpu 0.272 total

*/