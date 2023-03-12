#include <stdio.h>
#include <math.h> //Để sử dụng hàm toán học ceil
int main() {

unsigned long sotien;

    float sokm;
    printf("\n Ban hay cho biet so km da di duoc : "); scanf("%f", &sokm);
    if (sokm <= 1.0)
        sotien = 10000;
    else
        if (sokm <= 31.0)

            sotien = 10000+ (ceil(sokm) - 1.0) * 8000;

        else

            sotien = 250000+ (ceil(sokm) - 31) * 6000;
    printf("\n So tien can tra = %lud \n", sotien);
    return 0;

}
