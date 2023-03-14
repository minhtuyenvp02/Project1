//#include<stdio.h>
//int UCLN2So(int x, int y)
//{
//    if (x % y == 0)
//        return y;
//    return UCLN2So(y, x % y);//dùng đệ quy tìm ƯCLN của 2 số bằng thuật toán Euclid
//}
//int UCLN(int a[], int n)
//{
//    int UCLN = a[0];
//    for (int i = 1; i < n; i++)
//    {
//        UCLN = UCLN2So(UCLN, a[i]);
//    }
//    return UCLN;
//}
//int main(){
//    int n;
//    int a[10000];
//    printf("Nhập số phần tử của mảng n = ");
//    scanf("%d", &n);
//    printf("Nhập các phần tử của mảng:");
//    for(int i =0; i < n; i++){
//        scanf("%d", &a[i]);
//    }
//    int ans = UCLN(a, n);
//    printf("Ước chung lớn nhất của các phần tử trong mảng là: %d\n", ans);
//    return 0;
//}
