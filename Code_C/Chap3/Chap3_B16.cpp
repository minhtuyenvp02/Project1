///*
// Bài 16: Cài đặt thuật toán Bubble Sort
// */
//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int n, arr[100010];
//
//void inputArray(){
//  cin >> n;
//  for(int i = 0;i < n;i++) cin >> arr[i];
//}
//
//void swap(int *xp, int *yp)
//{
//    int temp = *xp;
//    *xp = *yp;
//    *yp = temp;
//}
//  
//void bubbleSort(int arr[], int n)
//{
//   int i, j;
//   bool swapped;
//   for (i = 0; i < n-1; i++)
//   {
//     swapped = false;
//     for (j = 0; j < n-i-1; j++)
//     {
//        if (arr[j] > arr[j+1])
//        {
//           swap(&arr[j], &arr[j+1]);
//           swapped = true;
//        }
//     }
//     if (swapped == false)
//        break;
//   }
//}
//  
//
//void printArray(int arr[], int n)
//{
//    for (int i = 0; i < n; i++)
//        cout << arr[i] << " ";
//    cout << "\n";
//}
//
//int main()
//{
//    inputArray();
//    bubbleSort(arr, n);
//    printArray(arr, n);
// 
//    return 0;
//}
//
