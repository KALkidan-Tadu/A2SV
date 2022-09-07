class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        priority_queue<pair<int, string>>minheap;
        map<string, int> count;
        vector<pair<int,string>> candidates;
        vector<string> answer;
        for(string &word : words)
            count[word]++;
        for(auto &i : count){
            minheap.push({-i.second, i.first});
            if(minheap.size()>k)
                minheap.pop();
        }
        while(!minheap.empty()){
            candidates.push_back(minheap.top());
            minheap.pop();
        }
        sort(candidates.begin(), candidates.end());
        for(auto & c : candidates)
            answer.push_back(c.second);
        return answer;
    }
};
