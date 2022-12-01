class Counter
{
    int cnt{0};

public:
    void increment()
    {
        ++cnt;
    }
    int decrement()
    {
        return --cnt;
    }
    int count()
    {
        return cnt;
    }
};

template <class T>
class SmartPointer
{
    T *ptr;
    Counter *cnt;

public:
    SmartPointer(T *p = nullptr) : ptr{p}, cnt{new Counter()}
    {
        cnt->increment();
    }

    ~SmartPointer() { delete (ptr); }

    T &operator*() { return *ptr; }

    T *operator->() { return ptr; }
};
