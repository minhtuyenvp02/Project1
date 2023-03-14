///*
// Bài 18: Viết chương trình nhập vào một ma trận vuông,
// các phần tử nguyên, sau đó
// • Đưa ra ma trận tam giác duới
// • Đưa ra ma trận tam giác trên
// */
//#include <stdio.h>
//int main(){
//    int A[20][20], N,i,j;
//    printf("Nhap kich thuoc : "); scanf("%d",&N);
//    printf("\n");
//    for ( i=0; i < N; i++ )
//        for(j=0; j < N; j++) {
//            printf("Nhap phan tu [%d,%d]:", i+1,j+1);
//            scanf("%d", &A[i][j] );
//    }
//    printf("\n\n MA TRAN DA NHAP \n\n");
//    for ( i=0; i < N; i++ ){
//        for(j=0; j < N; j++)
//            printf( "%4d" ,A[i][j]);
//        printf("\n");
//    }
//    printf("\n\n MA TRAN TAM GIAC TREN \n\n");
//    for ( i=0; i < N; i++ ){
//        for(j=0; j < N; j++)
//            if(j >= i)
//                printf( "%4d" ,A[i][j]);
//            else
//                printf("%4c",32); //32 là mã ASCII của dấu cách
//        printf("\n");
//    }
//    printf("\n\n MA TRAN TAM GIAC DUOI \n\n");
//    for ( i=0; i < N; i++ ){
//        for(j=0; j <= i; j++)
//            printf( "%4d" ,A[i][j]);
//        printf("\n");
//    }
//}//main
//
//
