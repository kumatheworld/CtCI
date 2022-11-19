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
