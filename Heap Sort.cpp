void heapify(int arr[], int n, int i) {
    // Find largest among root, left child and right child
    int root = i;
    int leftchild = root*2 +1;
    int rightchild = root*2 +2;
    if(leftchild<n && arr[leftchild] > arr[root]){
        root = leftchild;
    }if(rightchild < n && arr[rightchild]>arr[root]){
        root = rightchild;
    }if(root != i){
        int temp = arr[root];
        arr[root] = arr[i];
        arr[i] = temp;
        heapify(arr, n, root);
    }
}

// Main function to do heap sort
void buildHeap(int arr[], int n) {
    // Build max heap
    for(int i=n/2 -1; i>=0; i--){
        heapify(arr, n, i);
    }
    for(int i=n-1; i>=0; i--){
        int temp = arr[i];
        arr[i] = arr[0];
        arr[0] = temp;
        heapify(arr, i, 0);
    }
    
}
