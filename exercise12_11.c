#include <stdlib.h>
#include <stdio.h>

void **my2DAlloc(int m, int n, size_t _SizeOfElements)
{
    void **a = (void **)malloc(m * sizeof(void *));

    a[0] = malloc(m * n * sizeof(_SizeOfElements));

    for (int i = 1; i < m; i++)
    {
        a[i] = (char *)a[0] + i * n * _SizeOfElements;
    }

    return a;
}

void my2DFree(void **a, int m)
{
    free(a[0]);
    free(a);
}

int main(void)
{
    int m = 3;
    int n = 4;
    int **a = (int **)my2DAlloc(m, n, sizeof(int));

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            a[i][j] = 0;
        }
    }

    my2DFree((void **)a, m);

    return 0;
}
