class Solution {
public:
    int minPairSum(vector<int>& nums) {
        vector<int> sums;
        sort(nums.begin(), nums.end());
        int half = nums.size()/2;
        int i = 0;
        int j = nums.size()-1;
        while(i < half){
             int sum = nums[i] + nums[j];
             sums.push_back(sum);
             i++;
             j--;
        }
        int max = sums[0];
        for(int i=1; i<sums.size(); i++){
            if(sums[i] > max)
                max = sums[i];
        }
        return max;
    }
};
