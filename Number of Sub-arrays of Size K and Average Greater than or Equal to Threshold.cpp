class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int subArrays = 0, right=0, left=0;
        long sum = 0;
        while(right<k)
            sum += arr[right++];
        if(sum/k >= threshold)
            subArrays++;
        while(right<arr.size()){
            sum = sum - arr[left++] + arr[right++];
            if(sum/k>= threshold)
                subArrays++;
        }
        return subArrays;
    }
};
