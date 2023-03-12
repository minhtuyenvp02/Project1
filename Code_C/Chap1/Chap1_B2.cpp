#include "stdio.h"
#include "math.h"
#define PI 3.14
int main(){
    float r;
    do{
        printf("Nhập r: ");
        scanf("%f", &r);
    }while(r < 0);
    
    float P = 2 * r * PI;
    float S = r * r * PI;
    
    printf("Chu vi đường tròn là: %.2f\n", P);
    printf("Diện tích đường tròn là: %.2f\n", S);
    return 0;
}
