class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> lastindex;
        vector<int> answer;
         for(int i=s.length()-1; i>=0; i--){
             if(lastindex.find(s[i])==lastindex.end())
                 lastindex[s[i]] = i;
         }
        int left=0, right=0;
        for(int i=0; i<s.length(); i++){
            right = max(right, lastindex[s[i]]);
            if(right==i){
                answer.push_back(i-left+1);
                left = i+1;
            }
        }
        return answer;
    }
};
