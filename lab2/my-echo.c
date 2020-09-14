#include<stdio.h>

int main(int argc, char *argv[]) {
    // printf("name: %s argc: %d\n", argv[0], argc);

    for(int i=1; i<argc; ++i) {
        printf("%s ",argv[i]);
    }
    printf("\n");
    return 42;
}
