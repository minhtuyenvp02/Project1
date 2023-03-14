//#include <stdio.h>
//#include<math.h>
//typedef struct{
//    float x;
//    float y;
//} Diem;
//
//int main(){
//    Diem A,B,C;
//    printf("Nhập toạ độ điểm A: ");
//    scanf("%f%f", &A.x,&A.y);
//    printf("Nhập toạ độ điểm B: ");
//    scanf("%f%f", &B.x,&B.y);
//    printf("Nhập toạ độ điểm C: ");
//    scanf("%f%f", &C.x,&C.y);
//    float AB = sqrt((A.x - B.x)*(A.x - B.x) + (A.y-B.y) * (A.y-B.y));
//    float AC = sqrt((A.x - C.x)*(A.x - C.x) + (A.y-C.y) * (A.y-C.y));
//    float BC = sqrt((B.x - C.x)*(B.x - C.x) + (B.y-C.y) * (B.y-C.y));
//    if((AB + BC > AC) && (AC + BC > AB) && (AB + AC > BC)){
//        float p = (AB + AC + AC)/2;
//        float s = sqrt(p*(p-AB)*(p-AC)*(p-BC));
//        printf("Diện tích tam giác là: %.3f\n", s);
//    } else printf("Không phải là tam giác.\n");
//    return 0;
//
//}
