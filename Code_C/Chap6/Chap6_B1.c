/*
 Bài 1:
 */
#include <stdio.h>
#include <string.h>
   typedef struct {
     char Ten[30];
     long SBD;
     char Khoa[10];
     float Diem;
} SinhVien;

int main() {
    FILE *f1;
    SinhVien SV;
    int i;
//Nhap thong tin cho file ThiSinh.Dat
    f1 = fopen("ThiSinh.Dat", "wb");
    i = 1;
    do {
        printf("Thi sinh %d :\n", i);
        printf(" Ho Ten : "); fflush(stdin); fgets(SV.Ten, sizeof(SV.Ten), stdin);
        SV.Ten[strlen(SV.Ten)-1] = '\0'; // Bỏ ký tự xuống dòng
        if(strcmp(SV.Ten,"***") == 0) break;
        printf(" So Bao Danh: "); scanf("%d", &SV.SBD);
        printf(" Khoa : "); fflush(stdin); fgets(SV.Khoa, sizeof(SV.Khoa), stdin);
        SV.Khoa[strlen(SV.Khoa) -1] = '\0'; // Bỏ ký tự xuống dòng
        printf(" Diem : "); scanf("%f", &SV.Diem);
        fwrite(&SV, sizeof(SinhVien), 1, f1);
        i++;
    } while(1);
    fclose(f1);

//In danh sach ban dau
    printf("\n\n DANH SACH BAN DAU \n");
   f1 = fopen("ThiSinh.Dat", "rb");
   i = 0;
   while (fread(&SV, sizeof(SinhVien), 1, f1) > 0)
    printf("%-3d %-5d %-20s %-20s %-5.1f\n", ++i, SV.SBD, SV.Ten, SV.Khoa, SV.Diem);
    fclose(f1);
    return 0;
}

