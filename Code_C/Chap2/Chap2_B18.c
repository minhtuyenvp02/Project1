#include <stdio.h>

int main(){
    int suma=0;
    char c;
    while((c = getchar()) != '*'){
        if(c == 'a' || c == 'A')
            suma++;
    }
    printf("Số lần suất hiện kí tự a là: %d\n", suma);
    return 0;
}
