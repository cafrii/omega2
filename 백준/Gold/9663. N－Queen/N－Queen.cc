
#include <cstdio>
#include <cmath>
typedef long long llong_t;

int A[15] = {0, };
int N = 0;
llong_t _count = 0;

// N 개의 row 로 구성된 board A 에 N 개의 queen 을 배치해야 하므로
// 최소한 row 1개에 하나의 queen 을 배치해야 한다.
bool IsAllowed(int row, int col)
{
    // board 의 (row,col) 위치에 새 queen 을 배치하기 전, 허용 가능 여부 검사
    for (int r=row-1; r>=0; r--) {
        if (A[r] == col || abs(A[r]-col) == row-r)
            return false;
    }
    return true;
}

void Backtrack(int index)
{
    // A[index] 번째의 row 에서 queen 의 위치 결정
    if (index >= N) {
        _count++; return;
    }
    for (int k=0; k<N; k++) {
        // A[index][k] 에 queen 배치가 가능한지 체크하고, 가능하다면 후속 호출.
        if (! IsAllowed(index, k))
            continue;
        A[index] = k;
        Backtrack(index+1);
    }
}

llong_t Solve(int N)
{
    _count = 0;
    for (int i=0; i<N; i++) A[i] = -1;

    Backtrack(0); // 0번 row 부터 배치.
    return _count;
}

int main()
{
    scanf("%d", &N);
    printf("%lld\n", Solve(N));
    return 0;
}