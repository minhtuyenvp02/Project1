/*
bài 14: Tìm số có 3 chữ số abc thoả mãn abc = a^3 + b^3 + c^3
*/

#include "stdio.h"

int main(){
    
    for(int x = 100; x<1000; x++){
        int a = x / 100;
        int b = (x % 100) / 10;
        int c = x % 100 % 10;
            if(a * a * a + b * b * b + c * c * c == x)
                printf("%d\n", x);
    }
    return 0;
}
