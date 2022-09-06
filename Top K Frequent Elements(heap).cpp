class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>>minheap;
        vector<int> answer;
        unordered_map<int, int> count;
        for(int i =0; i<nums.size(); i++){
            count[nums[i]]++;
        }
        for(auto &c : count){
            minheap.push({c.second, c.first});
            if(minheap.size()>k)
                minheap.pop();
        }
        while(k--){
            answer.push_back(minheap.top().second);
            minheap.pop();
        }
        return answer;
    }
};
