int select(int arr[], int i)
{
    return arr[i];
} // code here such that selecionSort() sorts arr[]



void selectionSort(int arr[], int n)
{
   for(int i=0; i<n-1; i++){
      for(int j=i+1; j<n; j++){
          if(arr[j]<arr[i]){
              int temp = arr[j];
              arr[j] = arr[i];
              arr[i] = temp;
          }
      }
   }
  //code here
}
