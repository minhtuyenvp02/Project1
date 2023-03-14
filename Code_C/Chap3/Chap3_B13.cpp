///*
// Bài 13: Cài đặt thuật toán quick_Sort
// */
//
//#include<iostream>
//#include<algorithm>
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
//int partition(int arr[], int low, int high)
//{
//    int pivot = arr[high];
//    int i = (low - 1);
// 
//    for (int j = low; j <= high - 1; j++) {
//        if (arr[j] < pivot) {
//            i++;
//            swap(arr[i], arr[j]);
//        }
//    }
//    swap(arr[i + 1], arr[high]);
//    return (i + 1);
//}
// 
//void quickSort(int arr[], int low, int high)
//{
//    if (low < high) {
//        int pi = partition(arr, low, high);
//        quickSort(arr, low, pi - 1);
//        quickSort(arr, pi + 1, high);
//    }
//}
// 
//void printArray(int arr[], int size)
//{
//    int i;
//    for (i = 0; i < size; i++)
//        cout << arr[i] << " ";
//    cout << endl;
//}
//
//int main()
//{
//    inputArray();
//    quickSort(arr, 0, n - 1);
//    printArray(arr, n);
//    return 0;
//}
// 
