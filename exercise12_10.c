#include <stdlib.h>

char *align_malloc(size_t _Size, int div)
{
    char *p = (char *)malloc(_Size + div);
    // Wanna free some initial segment of p, but is that possible?
    return p;
}

void aligned_free(char *_Memory)
{
    free(_Memory);
}
