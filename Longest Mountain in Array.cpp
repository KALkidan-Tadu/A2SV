class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int longest = 0, start=0, end=0;
        while(end<arr.size()){
            while(start<arr.size()-1 && arr[start+1]<=arr[start]){
                start++;
                end++;
            }
            while(end<arr.size()-1 && arr[end+1]>arr[end]){
                end++;
            }
            while(end<arr.size()-1 && arr[end+1]<arr[end]){
                end++;
                longest = max(longest, end-start+1);
            }
            end++;
            start = end-1;
        }
        return longest;
    }
};
