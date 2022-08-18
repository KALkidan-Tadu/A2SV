class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i=0, j;
        if(nums.size()%2==0)
            j=nums.size()-1;
        else
            j=nums.size()-2;
        while(i<nums.size()/2 && j>=nums.size()/2){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i+=2;
            j-=2;
        }
        return nums;
    }
};
