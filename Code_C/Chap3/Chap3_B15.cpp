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
//void selectionSort(int arr[], int n)
//{
//    int i, j, min_idx;
//    for (i = 0; i < n-1; i++)
//    {
//        min_idx = i;
//        for (j = i+1; j < n; j++)
//        {
//          if (arr[j] < arr[min_idx])
//              min_idx = j;
//        }
//        if (min_idx!=i)
//            swap(&arr[min_idx], &arr[i]);
//    }
//}
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
//    selectionSort(arr, n);
//    printArray(arr, n);
// 
//    return 0;
//}
//
//
