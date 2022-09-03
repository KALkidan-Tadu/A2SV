class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int> order;
        int i= 0, j=0, answer=0;
        while(i<nums.size()){
            order.insert(nums[i]);
            i++;
            while(true){
                if(abs(*order.begin() -*order.rbegin()) > limit){
                    auto index = order.find(nums[j]);
                    order.erase(index);
                    j++;
                    continue;
                }
                break;
            }
            int s = order.size();
            answer = max(answer, s);
        }
        return answer;
    }
};
