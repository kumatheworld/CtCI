#include <cstring>
#include <algorithm>

void reverse(char *str)
{
    int n = std::strlen(str);
    std::reverse(str, str + n);
    for (int i = 0; i < n / 2; ++i)
    {
        --j;
        char c = str[i];
        str[i] = str[j];
        str[j] = c;
    }
}
