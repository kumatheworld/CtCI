#include <cstring>

void reverse(char *str)
{
    int n = std::strlen(str);
    int j = n;
    for (int i = 0; i < n / 2; ++i)
    {
        --j;
        char c = str[i];
        str[i] = str[j];
        str[j] = c;
    }
}
