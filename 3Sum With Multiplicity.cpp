class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int mod = pow(10,9)+7;
        int answer = 0;
        sort(arr.begin(), arr.end());
        for(int i=0; i<arr.size(); i++){
            int left = i+1;
            int right = arr.size()-1;
            int k = target - arr[i];
            while(left<right){
                if(arr[left]+arr[right]==k){
                    int c1=1, c2=1;
                   if(arr[left]==arr[right]){
                       answer += (right-left+1) * (right-left) / 2;
                       answer %= mod;
                       break;
                   }else{
                       while(left+1 < right && arr[left]==arr[left+1]){
                           c1++;
                           left++;
                       }
                       while(right-1>left && arr[right]==arr[right-1]){
                           right--;
                           c2++;
                       }
                       answer += c1*c2;
                       answer %= mod;
                       left++;
                       right--;
                   }
                }else if(arr[left]+arr[right]>k)
                    right--;
                else
                    left++;
            }
        }
        return answer;
    }
};
