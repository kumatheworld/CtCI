// I owe most of this file to the following website.
// https://www.acodersjourney.com/implementing-smart-pointer-using-reference-counting/
#include <iostream>

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

    ~SmartPointer()
    {
        if (cnt)
        {
            if (cnt->decrement() <= 0)
            {
                delete cnt;
                delete ptr;
                cnt = nullptr;
                ptr = nullptr;
            }
        }
    }

    SmartPointer(const SmartPointer<T> &other)
        : ptr{other.ptr}, cnt{other.cnt}
    {
        cnt->increment();
    }

    SmartPointer<T> &operator=(const SmartPointer<T> &other)
    {
        if (this != &other)
        {
            if (cnt)
            {
                if (cnt->decrement() <= 0)
                {
                    delete cnt;
                    delete ptr;
                }
            }
            ptr = other.ptr;
            cnt = other.cnt;
            cnt->increment();
        }
        return *this;
    }

    T &operator*() { return *ptr; }

    T *operator->() { return ptr; }
};

class Something
{
    std::string name;

public:
    Something(const std::string &n) : name{n}
    {
        std::cout << "Creating object: " << n << "\n";
    }
    ~Something()
    {
        std::cout << "Deleting object: " << name << "\n";
    }
};
