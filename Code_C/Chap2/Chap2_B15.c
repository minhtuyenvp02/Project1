/* Tính tổng n số tự nhiên đầu tiên*/
#include <stdio.h>
int main() {
    int n;
    printf("Nhập n:"); scanf("%d", &n);
    long long sum=0;
    for(int i=0; i<n; i++){
        sum+=i;
    }
    printf("%ld\n", sum);
    return 0;
}
