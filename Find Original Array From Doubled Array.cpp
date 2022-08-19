class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        unordered_map<int, int> count;
        vector<int> answer;
        vector<int> empty;
        int n = changed.size();
        sort(changed.begin(), changed.end());
        for(int i=0; i<changed.size(); i++){
            count[changed[i]]++;
        }
        for(int i=0; i<changed.size(); i++){
            int freq= count[changed[i]];
            if(freq>0){
                int twice= changed[i]*2;
                answer.push_back(changed[i]);
                count[changed[i]]--;
                count[twice]--;
            }
        }
        if(answer.size()== n/2)
            return answer;
        return empty;
    }
};
