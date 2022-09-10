#include <stdio.h>
#include <stdlib.h>
int main()
{
    char *ptr;
    int n;
    int chars;
    printf("entre the no. of employee  :-");
    scanf("%d", &n);

    for (int i = 1; i < n + 1; i++)
    {
        printf("please enter the id of %d no. employee", i);
        scanf("%d", &chars);
        ptr = (char *)malloc((chars + 1) * sizeof(char));
        scanf("%s", ptr);
        printf("the id of %d no. employee is %s\n", i, ptr);
        
    }
    return 0;

}  