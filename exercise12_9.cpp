class Counter
{
    int cnt{0};

public:
    void increment()
    {
        ++cnt;
    }
    void decrement()
    {
        --cnt;
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

    ~SmartPointer()
    {
        if (cnt)
        {
            cnt->decrement();
            if (cnt->count() <= 0)
            {
                delete cnt;
                delete ptr;
                cnt = nullptr;
                ptr = nullptr;
            }
        }
    }

    T &operator*() { return *ptr; }

    T *operator->() { return ptr; }
};
