#include <cstring>
#include <algorithm>
#include <iostream>

void reverse(char *str)
{
    int n = std::strlen(str);
    std::reverse(str, str + n);
}

int main()
{
    char str[] = "Cracking the Coding Interview";
    reverse(str);
    std::cout << str << std::endl;
}
