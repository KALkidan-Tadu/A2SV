class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
       sort(nums.begin(), nums.end());
       long left=0, right=0, total=0, max=0;
       while(right<nums.size()){
           total+=nums[right];
           while(nums[right]*(right-left+1)>total+k){
               total-=nums[left];
               left++;
           }
           if((right-left+1)>max)
               max = right-left+1;
           right++;
    }
        return max;
    }
};
