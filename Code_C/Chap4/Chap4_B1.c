/*
 Bài 1: Nhập vào một số phức đưa ra tổng của chúng
 */
#include <stdio.h>

    typedef struct {float re, im;} Complex;
int main(){
    Complex R, R1, R2;
    printf("Phan thuc & phan ao cho so thu nhat: "); scanf("%f%f",&R1.re,&R1.im);
    printf("Phan thuc & phan ao cho so thu hai: "); scanf("%f%f",&R2.re,&R2.im);
    R.re = R1.re+R2.re; R.im = R1.im+R2.im; // Phep cong so ao
    printf("(%.1f+%.1fi)+(%.1f+%.1fi)=(%.1f+%.1fi)\n",
                     R1.re,R1.im,R2.re,R2.im,R.re,R.im);
    R.re = R1.re*R2.re - R1.im*R2.im; // Nhan so ao
    R.im = R1.re*R2.im + R1.im*R2.re;
        printf("(%.1f+%.1fi)*(%.1f+%.1fi)=(%.1f+%.1fi)\n",
               R1.re,R1.im,R2.re,R2.im,R.re,R.im
               );
               
    return 0;
}

