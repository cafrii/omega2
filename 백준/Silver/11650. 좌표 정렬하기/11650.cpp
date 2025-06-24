/*



*/



#include <iostream>
#include <algorithm>


using namespace std;

int main()
{
    int n, x, y;
    scanf("%d", &n);

    using elm = pair<int,int>;
    vector<elm> arr(n);

    for (int i=0; i<n; i++) {
        scanf("%d%d", &arr[i].first, &arr[i].second);
    }
    using celm = const elm&;
    sort(arr.begin(), arr.end(), [](celm p1, celm p2){
        return (p1.first < p2.first) ||
            (p1.first == p2.first && p1.second < p2.second);
    });
    for (auto& p: arr) {
        printf("%d %d\n", p.first, p.second);
    }
    return 0;
}


/*
clang++ -std=c++17 -o out/a 11650.cpp

run=out/a

$run

*/
