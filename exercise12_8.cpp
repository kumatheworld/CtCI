template <class T>
class Node
{
public:
    T data;
    Node<T> *left;
    Node<T> *right;

    Node(T d)
    {
        data = d;
        left = nullptr;
        right = nullptr;
    }
};
