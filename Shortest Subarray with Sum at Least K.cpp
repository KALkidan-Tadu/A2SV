class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        int answer = INT_MAX;
        deque<int> q;
        vector<long> sums(n+1);
        for(int i=0; i<nums.size(); i++){
            sums[i+1] = sums[i]+ (long)nums[i];
        }
        for(int j = 0; j<sums.size(); j++){
            while(q.size() && sums[j]<=sums[q.back()])
                q.pop_back();
            while(q.size() && sums[j] >=sums[q.front()]+k){
                answer = min(answer, j-q.front());
                q.pop_front();
            }
            q.push_back(j);
        }
        if (answer == INT_MAX)
            return -1; 
        return answer;
    }
};
