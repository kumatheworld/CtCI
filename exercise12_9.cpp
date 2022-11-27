class Counter
{
private:
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

public:
    SmartPointer(T *p = nullptr) { ptr = p; }

    ~SmartPointer() { delete (ptr); }

    T &operator*() { return *ptr; }

    T *operator->() { return ptr; }
};
