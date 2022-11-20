#include <iostream>

template <class T>
class Node
{
public:
    T data;
    Node<T> *left;
    Node<T> *right;

    Node(T d) : data(d), left(nullptr), right(nullptr) {}
};

template <class T>
Node<T> *copy(Node<T> *p)
{
    if (p == nullptr)
    {
        return nullptr;
    }

    Node<T> *q = new Node<T>(p->data);
    q->left = copy(p->left);
    q->right = copy(p->right);
    return q;
}

template <typename T>
std::ostream &operator<<(std::ostream &outs, const Node<T> n)
{
    outs << n.data << " ";
    if (n.left)
    {
        outs << *n.left;
    }
    if (n.right)
    {
        outs << *n.right;
    }

    return outs;
}

int main()
{
    Node<int> *p = new Node(1);
    p->left = new Node(2);
    p->right = new Node(3);
    p->right->left = new Node(4);

    Node<int> *q = copy(p);
    q->right->data = 5;
    std::cout << *p << "\n"
              << *q << "\n";

    return 0;
}
