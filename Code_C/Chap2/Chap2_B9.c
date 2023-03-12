/*
Bài9:  Lập trình đọc tọa độ 4 điểm A,B,C,M rồi kiểm tra
xem điểm M nằm trong, nằm trên cạnh hay nằm
ngoài tam giác ABC.
*/

#include<stdio.h>
#include<math.h>
typedef struct {
    float x;
    float y;
}Diem;

int check_khac_phia(Diem A, Diem B, Diem C, Diem M){

    float a = B.x - A.x;
    float b = B.y - A.y;
    if(a == 0 && b == 0){
        printf("Không là tam giác!");
        return 0;
    }
        
    else if(!a){
        if((M.x - A.x) * (C.x - A.x) == 0) return 0;
        else if ((M.x - A.x) * (C.x - A.x) < 0) return -1;
        else return 1;
    }
    else if(!b){
        if((M.y - A.y) * (C.y - A.y) == 0) return 0;
        else if ((M.y - A.y) * (C.y - A.y) < 0) return -1;
        else return 1;
    }
    else{
        float fC, fM;
        fC =(C.x - A.x) / a - (C.y - A.y) / b;
        fM =(M.x - A.x) / a - (M.y - A.y) / b;
        if(fC * fM < 0)
            return -1;
        else if(fC * fM == 0)
            return 0;
        else
            return 1;
    }
}

int main(){
    Diem A, B, C, M;
    printf("Nhập toạ độ điểm A, B, C và M: ");
    printf("Nhập toạ độ điểm A: "); scanf("%f %f", &A.x, &A.y);
    printf("Nhập toạ độ điểm B: "); scanf("%f %f", &B.x, &B.y);
    printf("Nhập toạ độ điểm C: "); scanf("%f %f", &C.x, &C.y);
    printf("Nhập toạ độ điểm M: "); scanf("%f %f", &M.x, &M.y);
    int a,b,c;
    a = check_khac_phia(B, C, A, M);
    b = check_khac_phia(A, C, B, M);
    c = check_khac_phia(A, B, C, M);
    if(a * b * c == 0)
        if(!a)
            printf("M nằm trên cạnh BC\n");
        else if (!b)
            printf("M nằm trên cạnh AC\n");
        else
            printf("M nằm trên cạnh AB\n");
    else if ((a * b < 0) || (b * c < 0) || (a * c < 0))
        printf("M nằm ngoài tam giác ABC\n");
    else
        printf("M nằm trong tam giác ABC \n");
    
    return 0;
}

