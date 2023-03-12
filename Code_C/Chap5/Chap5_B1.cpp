/*
 Bài1: Giải phương trình f(x)=0 trên đoạn [a,b]
 f(x) = x^3 - x - 1
 
 */
#include <stdio.h>
#include <math.h>
float f(float x) {
  return x*x*x-x-1;
}
int main() {
    float a =1.0, b= 2.0, c, eps = 1.0e-6;
     do{
        c =(a+b) / 2;
        if(f(a)*f(c)<0)b=c;
        else a = c;
    }while(fabs(b-a)>eps);
    printf("Nghiemla:%.6f \n",(b+a)/2);
    return 0;
}

