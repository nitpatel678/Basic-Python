#include<stdio.h>
#include<stdlib.h>
int main () {
    int i,n;
    printf("Enter the no:");
    scanf("%d", &n);
    int *ptr = (int *)malloc(n*sizeof(int));
    if(ptr == NULL){
        printf("Memory location not found!");
        exit(1);
    }
    for ( i = 0; i < n; i++)
    {
        printf("Enter the numbers:");
        scanf("%d", &ptr+i);
    }
    for ( i = 0; i < n; i++)
    {
        printf("%d", *ptr);
    }
    

return 0;
}