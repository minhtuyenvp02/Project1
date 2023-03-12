/*
 Bài 23: Nhập dãy (<100) xâu cho tới khi gặp xâu “***”.
 Đưa ra màn hình xâu có độ dài lớn nhất
 */
#include <stdio.h>
#include <string.h>
int main(){
    int i, n = 0, d=0;
    char DS[100][30], s[30]="";
    do{
        printf("Nhap xau thu [%d]: ",n+1); gets(DS[n]);
        if( strcmp(DS[n],"***")) n= n + 1;//Không tính xâu “***”
        else break;
    }while(1);
    for(i = 0; i < n; i++)
        if(strlen(DS[i]) > d){
            d = strlen(DS[i]);
            strcpy(s,DS[i]);
            }
    printf("\n\nXau dai nhat la: %s \n Co do dai :%d\n",s,d);
}

