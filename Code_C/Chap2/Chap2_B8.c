/*1.Viết chương trình nhập vào một ký tự hệ hexa và đưa ra giá trị hệ 10 tương ứng*/
#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    int n;
    printf("Nhap N trong he thap luc phan: ");
    scanf("%x", &n);
    printf("Giá trị N trong he thap phan la: %d\n", n);
    
    return 0;
}
