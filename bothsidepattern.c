#include <stdio.h>
int main()
{
    int a, i, n, j;
    printf("entre how number of star you want to print");
    scanf("%d", &n);
    i = 0;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j <= n - i - 1; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
