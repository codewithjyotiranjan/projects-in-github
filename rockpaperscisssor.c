#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
int generateRandomNumber(int k)
{
    srand(time(NULL));
    return rand() % k;
}
int main()
{

    int a, b, c, w;

    b = 0;
    c = 0;

    char player1char, compchar;
    char dict[] = {'r', 'p', 's'};

    printf("enter your name\n");
    char name[100];
    scanf("%s", name);
    printf("your name is %s\n", name);
    printf("enter 8 for continue and 9 for break\n");
    scanf("%d", &w);

    while (w == 8)
    {
        printf("this is chance for player1\n");
        printf("enter 1 for paper,enter 2 for scisor,enter 3 for rock\n:-");
        scanf("%d", &a);
        player1char = dict[a - 1];
        printf("the enter chracter for player %s is %c\n", name, player1char);
        printf("this is chance for computer\n");
        int k = ("%d", generateRandomNumber(3));
        compchar = dict[(k - 1) + 1];
        printf("the enter chracter for computer is %c\n", compchar);

        if ((player1char == 'r') && (compchar == 'r'))
        {
            b += 0;
            c += 0;
            printf("match draw and score of  player1 is %d and computer is %d\n", b, c);
        }
        if ((player1char == 'r') && (compchar == 'p'))
        {
            c += 1;
            printf("computer win and got point is %d\n", c);
        }
        if ((player1char == 'r') && (compchar == 's'))
        {
            b += 1;
            printf("player win and got point is %d\n", b);
        }
        if ((player1char == 'p') && (compchar == 'r'))
        {
            b += 1;
            printf("player win and got point is %d\n", b);
        }
        if ((player1char == 'p') && (compchar == 'p'))
        {
            b += 0;
            c += 0;
            printf("match draw and score of  player1 is %d and computer is %d\n", b, c);
        }
        if ((player1char == 'p') && (compchar == 's'))
        {
            c += 1;
            printf("computer win and got point is %d\n", c);
        }
        if ((player1char == 's') && (compchar == 'r'))
        {
            c += 1;
            printf("computer win and got point is %d\n", c);
        }
        if ((player1char == 's') && (compchar == 'p'))
        {
            b += 1;
            printf("player win and got point is %d\n", b);
        }
        if ((player1char == 's') && (compchar == 's'))
        {
            b += 0;
            c += 0;
            printf("match draw and score of  player1 is %d and computer is %d\n", b, c);
        }
        printf("enter 8 for continue and 9 for break\n");
        scanf("%d", &w);

        if (w == 8)
        {
            continue;
        }
        if (w == 9)
        {
            goto end;
        }
    }
end:

    if (b > c)
    {
        printf("%s win this game\n",name);
    }
    if (c > b)
        printf("computer win this ganme\n");

    return 0;
}