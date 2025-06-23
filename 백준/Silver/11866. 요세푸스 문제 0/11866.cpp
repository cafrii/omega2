/*



*/


#include <iostream>
// #include <cstdio>

// #include "types/pyc_stringifier.hpp"

using namespace std;

vector<int> solve(int n, int k)
{
    vector<int> arr(n);
    vector<int> res;

    for (int i=0; i<n; i++)
        arr[i] = i+1;

    int idx = 0;
    k--;
    while (!arr.empty()) {
        idx = (idx + k) % (int)arr.size();
        res.push_back(arr[idx]);
        arr.erase(arr.begin() + idx);
    }
    return res;
}

int main()
{
    int n, k;

    scanf("%d%d", &n, &k);

    auto answer = solve(n, k);
    printf("<");
    for (int i=0; i<(int)answer.size(); i++) {
        if (i > 0)
            printf(", ");
        printf("%d", answer[i]);
    }
    printf(">\n");

    return 0;
}

/*
clang++ -std=c++20 -o out/a 11866.cpp



*/
