///*
// Bài 12: nHập vào mảng số nguyên n phần tử sắp xếp theo thứ tự tăng dần, giảm dần
// */
//#include<stdio.h>
// int main(){
//    int A[100] ;
//    int N, i, j , t;
//    printf("So phan tu [< 100]: "); scanf("%d",&N);
//    printf("Hay nhap day so...\n");
//    for(i=0; i < N; i++){
//         printf("A[%d] = ",i+1); scanf("%d",&A[i]);
//     }
//    printf("\nDay vua nhap...\n");
//    for(i=0; i < N; i++)
//        printf("%d ", A[i]);
//    printf("\n\n");
//    printf("Sap xep day theo thuat toan lua chon\n");
//     for(i=0; i < N-1; i++){
//         for(j=i+1; j < N; j++)
//             if(A[i] < A[j]) {
//                 t = A[i];
//                 A[i] = A[j];
//                 A[j] = t;
//             }
//     }
//     for(int i=0; i < N; i++)
//         printf(" %d ", A[i]);
//     return 0;
//}//main
//
