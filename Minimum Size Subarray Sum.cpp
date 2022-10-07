class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left=0, answer=INT_MAX, sum=0;
        for(int i=0; i<nums.size(); i++){
            sum += nums[i];
            while(sum>=target){
                answer = min(answer, i-left+1);
                sum -= nums[left];
                left++;
            }
        }
        if(answer == INT_MAX)
            return 0;
        return answer;
    }
};
