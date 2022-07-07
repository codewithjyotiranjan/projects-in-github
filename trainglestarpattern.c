#include <stdio.h>
int main()
{
    int a, i, n, j;
    printf("choose '0' for traingle pattern star or "
           "choose '1' for oppsite traingle pettern:-");
    scanf("%d", &a);
    printf("entre how number of line star you want to print:-");
    scanf("%d", &n);
    i = 0;
    if (a == 0)
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j <= i; j++)
            {
                printf("*");
            }
            printf("\n");
        }
    }
    if (a == 1)
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j <= n - i - 1; j++)
            {
                printf("*");
            }
            printf("\n");
        }
    }

    return 0;
}