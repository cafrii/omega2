/*
    다른 답안
    https://blog.naver.com/jinhan814/222610281029

*/

// #include <bits/stdc++.h>
#include <iostream>

#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
	fastio;
	int n, ans = 0, flag = 0; cin >> n;
	vector<int> v1, v2; // neg, pos
	for (int t; n-- && cin >> t;) {
		if (!t) flag = 1;
		else (t < 0 ? v1 : v2).push_back(t);
	}
	sort(v1.begin(), v1.end()), sort(v2.rbegin(), v2.rend());
    // vector<int> neg,pos;
	for (int i = 1; i < v1.size(); i += 2) {
        ans += v1[i - 1] * v1[i];
        // neg.push_back(v1[i - 1] * v1[i]);
    }
	for (int i = 1; i < v2.size(); i += 2) {
        ans += max(v2[i - 1] + v2[i], v2[i - 1] * v2[i]);
        // pos.push_back(max(v2[i - 1] + v2[i], v2[i - 1] * v2[i]));
    }
    // for (auto n: neg) { cout << n << " "; }
    // for (auto n: pos) { cout << n << " "; }
    // cout << endl;

	if (v1.size() & 1 && !flag) ans += v1.back();
	if (v2.size() & 1) ans += v2.back();
	cout << ans << '\n';
}

/*
clang++ -std=c++20 -o out/a 1744a.cpp

run=out/a
echo '42\n-282\n-865\n153\n-63\n-419\n48\n528\n-754\n-460\n-790\n125\n258\n-326\n386\n340\n-101\n225\n-805\n55\n-429\n-640\n-717\n-662\n88\n-41\n-538\n885\n-509\n791\n810\n-485\n938\n41\n104\n105\n-453\n556\n430\n155\n787\n-593\n-873' | $run
-> 5781092



_T=100

python3 <<EOF
import subprocess,sys,os
from random import seed,randint
def test(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["python3", "1744.py"], **kwargs)
    out1,_ = p1.communicate(inp)
    p2 = subprocess.Popen(args=["out/a"], **kwargs)
    out2,_ = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed!')
        print(f'inp: {inp}')
        print(f'out1: {out1.rstrip()}')
        print(f'out2: {out2.rstrip()}')
        assert False
    print(f'ok, {out1.rstrip()}')

T = int(os.getenv("_T", "1"))
for i in range(T):
    print(f'**** {i}/{T}')
    N = randint(1,50)
    A = [ f'{N}\n' ]
    for k in range(N):
        A.append(f'{randint(-1000,1000)}\n')
    inpstr = ''.join(A)
    test(inpstr)
print('done')
EOF



*/