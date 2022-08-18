vector<int> countingSort(vector<int> arr) {
    vector<int>freq(100, 0);
    for(int j=0; j<arr.size(); j++){
        int num = arr[j];
        freq[num]+=1;
    }
    return freq;
}
