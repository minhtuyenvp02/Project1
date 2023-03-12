#include <stdio.h>

int main(){

    float a, b; float max; // khai bao bien
    printf(" Nhap gia tri a và b: ");
    scanf("%f %f",&a, &b);
    if(a < b) max = b;
    else max = a;
    printf("\n So lon nhat trong 2 so %.4f và %.4f La %.4f \n",a,b,max);
    return 0;

} //ket thuc ham main()

