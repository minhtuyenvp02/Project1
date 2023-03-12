/*
 Bài 3:
 • Đưa ra DSSV đã sắp xếp theo kết quả thi
 • Đưa ra danh sách sinh viên dự thi khoa CNTT có điểm thi từ 22.5 trở lên
 • Nhập vào một số báo danh và in ra họ tên, điểm thi và khoa đăng ký
  của thí sinh nếu tìm thấy. Nếu không tìm thấy thí sinh thì
  đưa ra thông báo « không tìm thấy »
 */

#include<stdio.h>
#include<string.h>
typedef struct{
    int SBD;
    char Ten[30]; char Khoa[10]; float Diem;
}ThiSinh;
int main(){
    ThiSinh DS[100], SV;
    int N, i, j, d=0, SBD;
    char Ch; //Sử dụng trong thực hiện tìm kiếm nhiều lần
    printf("Nhap so thi sinh: "); scanf("%d", &N);
     for (i=0; i < N; i++) {
    printf("Nhap du lieu cho thi sinh %d: \n", i+1);
    printf("So bao danh: "); scanf("%d", &DS[i].SBD);
         
    printf("Ho ten: ");
    fflush(stdin); fgets(DS[i].Ten, sizeof(DS[i].Ten), stdin);
    DS[i].Ten[strlen(DS[i].Ten) - 1] = '\0'; // Bỏ ký tự xuống dòng
         
    printf("Khoa dang ky: ");
    fflush(stdin); fgets(DS[i].Khoa, sizeof(DS[i].Khoa), stdin);
    DS[i].Khoa[strlen(DS[i].Khoa) - 1] = '\0'; // Bỏ ký tự xuống dòng
         
    printf("Ket qua thi: "); scanf("%f", &DS[i].Diem);
    printf("\n");
    }//for
    printf("\n\nNhan phim bat ky de xem ket qua thi...");
    for(i=0;i<N-1;i++)//SắpxếpDStheođiểmthi
        for (j = i+1; j < N; j++)
            if (DS[i].Diem > DS[j].Diem) {
            SV = DS[i];
            DS[i] = DS[j];
            DS[j] = SV;
        }
    printf("\n\n            KET QUA THI \n\n");
    for(i=0;i<N;i++)
    printf("%-3d BKA- %-6d %-24s %-6s %-6.1f\n", ++d,
            DS[i].SBD, DS[i].Ten, DS[i].Khoa, DS[i].Diem);
    printf("\n\nNhan phim bat ky de xem DSSV khoa CNTT");

    do{
    printf("\nNhap so bao danh can tim: ");
    scanf("%d", &SBD);
    for(i=0;i<N; i++)
    if (DS[i].SBD == SBD) {
        printf("So bao danh : %d \n", SBD);
        printf("Ho ten : %s \n", DS[i].Ten);
        printf("Khoa du thi: %s \n", DS[i].Khoa);
        printf("So bao danh : %.1f \n", DS[i].Diem);
        break;
    }
    if(i==N)
        printf("So bao danh %d không tồn tại \n", SBD);
    
    printf("\n Co tiep tuc tim kiem nua khong (C/K): ");
        scanf("%s", &Ch);
    }while(Ch != 'K');
    
  return 0;
}//main

