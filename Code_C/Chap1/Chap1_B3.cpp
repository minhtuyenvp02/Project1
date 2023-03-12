#include "stdio.h"
#include "math.h"
#define PI 3.14
int main(){
    float a;
    do{
        printf("Nhập a: ");
        scanf("%f", &a);
    }while(a < 0);
    
    printf("Chu vi đường tròn là: %.2f\n", 2 * a * PI);
    printf("Chu vi tam giác đều là: %.2f\n", a * 3);
    printf("Chu vi hình vuông là: %.2f\n", a * 4);
    
    return 0;
}

