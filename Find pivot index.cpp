class Solution {
public:
    int pivotIndex(vector<int>& nums) { 
        vector<int>sum;
        sum.push_back(nums[0]);
        int n = nums.size();
        for(int i = 1 ; i<n ; i++)
        {
             sum.push_back(sum[i-1] + nums[i]);
        }
        if(sum[n-1] - sum[0] == 0)
            return 0;
        
        for(int i = 1 ; i<n ; i++)
        {
            if(sum[n-1] - sum[i] == sum[i-1])
                return i;
        }
        return -1;
    }
};
