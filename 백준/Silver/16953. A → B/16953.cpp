/*

c++ 연습용

12:27~12:44

*/

#include <iostream>
#include <deque>
#include <tuple>
using namespace std;

typedef long long llong_t;

llong_t solve(int A, int B)
{
    // max value 1e9 is within range of int32.
    deque< tuple<int,int> > que;
    que.push_back(tuple<int,int>{A, 1});

    while (!que.empty()) {
        auto [node, count] = que.front();
        que.pop_front();

        auto nexts = std::array<int, 2>{ node*10+1, node*2 };
        for (auto next: nexts) {
            if (next == B)
                return count+1;
            if (next > B)
                continue;

            que.push_back(tuple<int,int>{next, count+1});
        }
    }
    return -1;
}

int main()
{
    int A, B;
    cin >> A >> B;
    printf("%lld\n", solve(A, B));
    return 0;
}


/*
clang++ -std=c++17 -o out/a 16953.cc

*/
