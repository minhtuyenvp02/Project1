#include "stdio.h"

int main(){
    int N;
    printf("\n Nhap mot gia tri so nguyen khong am: "); scanf("%d",&N);
    switch(N) {
        case 1: printf("%d -> One \n",N); break;
        case 2: printf("%d -> Two \n",N); break;
        case 3: printf("%d -> Three \n",N); break;
        case 4: printf("%d -> Four \n",N); break;
        case 5: printf("%d -> Five \n",N); break;
        case 6: printf("%d -> Six \n",N); break;
        case 7: printf("%d -> Seven \n",N); break;
        case 8: printf("%d -> Eight \n",N); break;
        case 9: printf("%d -> Nine \n",N); break;
        case 10: printf("%d -> Ten \n",N); break;
    default : printf(" Khong thoa man dieu kien [1..10] \n");

    }
    return 0;
}
