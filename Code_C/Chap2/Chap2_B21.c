#include<stdio.h>
#include<math.h>
int main()
{
    //khai bao bien n
    int n;
    float x;
    //khai bao bien S
    float S;
    do{
        printf("Nhập x: ");
        scanf("%f", &x);
        if(x < 0){
            printf("x phải lớn hơn 0!");
        }
    }while(x < 0);
    
    do
    {
        printf("\nNhap n(n >= 1): ");
        scanf("%d", &n);
        if(n < 1)//neu N<1 yeu cau nhap lai
        {
            printf("\nn phai >= 1. Xin nhap lai !");
        }
    }while(n < 1);
    
    S = sqrt(x);//gan S = can bac hai cua x
    for(int i = 2; i <= n; i++)
    {
        S = sqrt(x + S);//gan S = can bac hai cua (x+S)
    }
    //in S ra man hinh
    printf("\nTong S = %f\n", S);
}
