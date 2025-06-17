#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int>> g_tree;
// vector element:
//   pair[0]: root node of this subtree is part of.
//   pair[1]: size of this subtree (number of nodes in this subtree)

const int kMOD = 1000000007;
// #define INT32_MAX 2147483647

/*
    return root node index
*/
int find_root(int node)
{
    while (g_tree[node].first != node)
        node = g_tree[node].first;
    return node;
}

void unify(int u, int v)
{
    // two node u, v will be in the same tree.
    int root1 = find_root(u);
    int root2 = find_root(v);
    if (root1 == root2) // already family
        return;

        // participate root2 as subtree of the tree of root1
    g_tree[root2].first = root1;
    // g_tree[root2].second = ... // no need to modify.
    // g_tree[root1].first = root1; // already root
    g_tree[root1].second += g_tree[root2].second;
}

int main()
{
    int n, m, u, v;
    scanf("%d%d", &n, &m);

    // for each node, remember root of tree where the node belongs.
    g_tree.reserve(n+1); // index 0 is not used.
    for (int k=0; k<=n; k++)
        // create [0] but we don't use it.
        g_tree.push_back({k, 1}); // single node tree. the node is also root.

    for (int k=0; k<m; k++) {
        scanf("%d%d", &u, &v);
        unify(u, v);
    }

    // for all root node of tree..
    int64_t answer = 1;
    for (int k=1; k<=n; k++) {
        if (g_tree[k].first == k) {
            answer = (answer * g_tree[k].second) % kMOD;
        }
    }
    printf("%d\n", (int)answer);
    return 0;
}
