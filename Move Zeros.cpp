class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 0)
                count++;
        }
        if(count == 0 || count == nums.size())
            return;
        int zero = 0, nonZ=0;
        while(nums[zero]!=0 && zero<nums.size())
                zero++;
        if(nums[zero]!= 0 || zero >= nums.size()-1)
                return;
        nonZ = zero+1;
        while(nums[nonZ]==0 && nonZ<nums.size())
                nonZ++;
        if(nums[nonZ]==0 || nonZ >= nums.size())
                return;
        while(nonZ<nums.size() && zero<nums.size()-1){
            while(nums[zero]!=0 && zero<nums.size()-1)
                zero++;
            if(zero>=nums.size()-1 || nums[zero]!=0)
                break;
            while(nums[nonZ]==0 && nonZ<nums.size()-1)
                nonZ++;
            if(nonZ>=nums.size() ||  nums[nonZ]==0)
                break;
            int temp = nums[zero];
            nums[zero] = nums[nonZ];
            nums[nonZ] = temp;
            nonZ++;
            zero++;
        }
        
    }
};
