#include "stdio.h"

int main(){
    int n;
    long long P = 1;
    printf("Nhập n: "); scanf("%d", &n);
    int i = 1;
    while(n >= i){
        P *= i;
        i++;
    }
    printf("%d! = %ld \n", n,P);
    return 0;
    
}
