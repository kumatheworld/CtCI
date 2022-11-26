template <class T>
class SmartPointer
{
    T *ptr;

public:
    SmartPointer(T *p = nullptr) { ptr = p; }

    ~SmartPointer() { delete (ptr); }

    T &operator*() { return *ptr; }

    T *operator->() { return ptr; }
};
