#include <stdlib.h>
#include <stdio.h>

typedef struct AlignedPointer
{
    char *ptr;
    int offset;
} AlignedPointer;

AlignedPointer align_malloc(size_t _Size, int div)
{
    AlignedPointer ap;
    char *p = (char *)malloc(_Size + div);

    char s[9];
    sprintf(s, "%x\n", p);

    long addr = strtol(s, NULL, 16);
    int offset = div - addr % div;

    ap.ptr = p + offset;
    ap.offset = offset;

    return ap;
}

void aligned_free(char *_Memory)
{
    free(_Memory);
}
