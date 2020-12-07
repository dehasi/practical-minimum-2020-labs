#include<stdio.h>

//  gcc factorial.c  -g -std=c99 -o factorial -Wformat=0
int main() {
    int num;
    do {
        printf("Enter a positive integer: ");
        scanf("%d", &num);
    } while (num < 0);

    int factorial;
    for(int i=0; i <= num; i++)
        factorial *= i;
    printf("%d! = %d\n", num, factorial);
}
