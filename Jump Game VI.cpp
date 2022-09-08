class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> answer(n);
        deque<int> q;
        answer[n-1] = nums[n-1];
        q.push_back(n-1);
        for(int i = n-2; i>=0; i--){
           if(q.front()-i>k)
               q.pop_front();
            answer[i] = nums[i] + answer[q.front()];
            while(q.size() && answer[q.back()]<answer[i])
                q.pop_back();
            q.push_back(i);
        }
        return answer[0];
    }
};
