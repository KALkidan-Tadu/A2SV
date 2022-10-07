class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int answer=0, del=0, left=0, right=0;
        while(right<nums.size()){
            if(nums[right] == 0)
                del++;
            while(del>1){
                if(nums[left]==0)
                    del--;
                left++;
            }
            right++;
            answer = max(answer, right-left-1);
        }
        return answer;
    }
};
