#include <stdlib.h>

void *align_malloc(size_t _Size, int div)
{
    void *p = malloc(_Size + div);
    // Wanna free some initial segment of p, but is that possible?
    return p;
}

void aligned_free(void *_Memory)
{
    free(_Memory);
}
