
#include <iostream>

using namespace std;

struct Node {
    int d;
    Node *lf, *rg; // left, right child

    Node(int d, Node* p=nullptr) {
        this->d = d;
        lf = rg = nullptr;
    }
};

void add_node(Node* tree, int d)
{
    if (d < tree->d) {
        if (tree->lf)
            add_node(tree->lf, d);
        else
            tree->lf = new Node(d);
    }
    else {
        if (tree->rg)
            add_node(tree->rg, d);
        else
            tree->rg = new Node(d);
    }
}

void print_postorder(Node* tree)
{
    if (tree->lf) print_postorder(tree->lf);
    if (tree->rg) print_postorder(tree->rg);
    printf("%d\n", tree->d);
}
void del_tree(Node* tree)
{
    if (!tree) return;
    if (tree->lf) del_tree(tree->lf);
    if (tree->rg) del_tree(tree->rg);
    tree->lf = tree->rg = nullptr;
    delete tree;
}

int main()
{
    int n;
    Node* root = nullptr;

    while (scanf("%d", &n) != EOF) {
        if (root)
            add_node(root, n);
        else
            root = new Node(n);
    }
    // print using post order
    print_postorder(root);

    del_tree(root);
    return 0;
}
