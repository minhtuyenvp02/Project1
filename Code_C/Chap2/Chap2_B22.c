///*
//Bài22: Lập chương trình tính sin(x) với độ chính xác nhập từ bàn phím theo công thức
//Sin(x) = x – x^3/3! + x^5/5! + … + (-1)^n . x^2n + 1/(2n + 1)!
//*/
//#include<stdio.h>
//#include<math.h>
//#define PI 3.1412
//#define eps 1e-4 // Sai số
//int main()
//{
//    float S, T, x, LuyThua, GiaiThua;
//    int i, Dau = -1;
//
//    printf("\nNhap x(độ): ");
//    scanf("%f", &x);
//    
//    x = x/180 * PI;
//
//    GiaiThua = 1;
//    S = T = LuyThua = x;
//    for(i = 3; T > eps; i += 2, Dau = -Dau)
//    {
//        T = (LuyThua *= x * x) / (GiaiThua *= i * (i - 1));
//        S += Dau * T;
//    }
//    printf("\nCong thuc Taylor: sin (%.2f) = %.4f\n", x, S);
//    printf("\nSin () cua math.h: sin(%.2f) = %.4f\n", x, sin(x));
//
//    return 0;
//}
//
//
