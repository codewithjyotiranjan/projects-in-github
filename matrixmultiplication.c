#include <stdio.h>
int main()
{
    printf("it is the 1st matrix\n");
    int m, n, i, j;
    printf("enter how many rows and colomn of matrix you want to create\n");
    printf("rows is\n");
    scanf("%d", &m);
    printf("coloumn is\n ");
    scanf("%d", &n);
    int matrix1[m][n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("enter number 1-9\n");
            scanf("%d", &matrix1[i][j]);
        }
    }
    printf("it is the second matrix\n");
    int k, l;
    printf("enter how many rows and colomn of matrix you want to create\n");
    printf("rows is\n");
    scanf("%d", &k);
    printf("coloumn is\n ");
    scanf("%d", &l);
    int matrix2[k][l];
    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j < l; j++)
        {
            printf("enter number 1-9\n");
            scanf("%d", &matrix2[i][j]);
        }
    }
    printf("\n");

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d\t", matrix1[i][j]);
        }
        printf("\n");
    }

    printf("\n");
    printf("-----------------------\n");
    printf("\n");

    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j < l; j++)
        {
            printf("%d\t", matrix2[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    int result[m][l], sum;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < l; j++)
        {
            for (int k = 0; k < n; k++)
            {
                sum += matrix1[i][k] * matrix2[k][j];
            }
            result[i][j] = sum;
            sum = 0;
            printf("\n");
        }
    }
    if (n == k)
    {
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < l; j++)
            {
                printf("%d\t", result[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("we can not multiply this");
    }

    return 0;
}