///*
// Bài 2: NHập vào một danh sách (<100) sinh viên gồm họ tên, năm sinh>
// Kết thúc nhập khi gặp sinh viên có tên là rỗng
//     _ Đưa ra danh sách vừa nhập ra màn hình
//     _ Đưa ra màn hình sinh viên lớn tuổi nhất
// */
//#include<stdio.h>
//#include<string.h>
//const int N=1000;
//typedef struct{
//        int NS;
//        char Ten[100];
//} SinhVien;
//SinhVien DS[N];
//int n;
//void input() {
//    for(n=0;n<N;n++){
//        printf("Nhập tên sinh viên thứ %d: \n", n + 1);
//        fflush(stdin);
//        fgets(DS[n].Ten, 100, stdin);
//        DS[n].Ten[strlen(DS[n].Ten) - 1] = '\0'; // Bỏ ký tự xuống dòng
//        if(strlen(DS[n].Ten) == 0)
//            break;
//        printf("Nam sinh: ");scanf("%d", &DS[n].NS);
//    }
//    return;
//}
//void output() {
//    // In danh sach sinh vien
//    printf("\n\n");
//    printf(" HO & TEN NAM SINH\n");
//    for(int i=0;i<n;i++)
//        printf("%-3d%-30s %6d\n", i+1, DS[i].Ten, DS[i].NS);
//    printf("\n\n");
//    return;
//}
//
//int main(){
//    input();
//    output();
//    SinhVien SV = DS[0];
//    // Tìm sinh viên lớn tuổi nhất
//    for(int i = 0; i<n; i++){
//        if(DS[i].NS < SV.NS)
//            SV = DS[i];
//    }
//    printf("Sinh viên lớn tuổi nhất là %s sinh năm %d \n", SV.Ten, SV.NS);
//    return 0;
//}
//    
//
