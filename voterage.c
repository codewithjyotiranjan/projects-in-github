#include <stdio.h>

int main()
{
    int age;
    printf("entre ur age\n");
    scanf("%d", &age);
    printf("u have entered %d as your age ,so\n", age);
    if (age > 18)
    {
        printf("you can vote");
    }
    else if (age < 18)
    {
        printf("you cannot vote");
    }
    else if (age == 18)
    {
        print("we will think about u");
    }
    else
    {
        printf( "error");
    }

    return 0;
}