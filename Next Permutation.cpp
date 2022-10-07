class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i=nums.size()-2, j;
        while(i>=0 && nums[i+1]<=nums[i])
            i--;
        if(i>=0){
            j = nums.size()-1;
            while(j>=0 && nums[j]<=nums[i])
                j--;
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        i++, j=nums.size()-1;
        while(i<j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
};
