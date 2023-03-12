#include <stdio.h>
int main(){
    float a, b;
    printf("\n Giai phuong trinh bac nhat ax + b = c");
    printf("\n Cho biet he so a b ");
    scanf("%f%f",&a, &b);
    if (a==0)
        if (b!=0)
            printf(" Phuong trinh vo nghiem \n");

        else printf(" Phuong trinh vo so nghiem \n");
    else
    printf(" Dap so cua phuong trinh tren = %f \n", -b/a);
    return 0;
}
