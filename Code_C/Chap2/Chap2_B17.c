#include<stdio.h>

int main(){
    int na=0, pa=0, kt=0;
    char c;
    printf(">> ");
    while ((c = getchar()) != '\n') {
        switch(c){
            case 'a': case 'e' : case 'u': case 'i': case 'o':
            case 'A': case 'E' : case 'U': case 'I': case 'O':
                na++;
                break;
            case ' ': kt++; break;
            default: pa++;
        }
    }
    printf("Số nguyên âm: %d\n", na);
    printf("Số phụ âm: %d\n", pa);
    printf("Số khoảng trắng: %d\n", kt);
    return 0;
}
