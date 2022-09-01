class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int l = questions.size();
        vector<long long> dynamic(l);
        for(int i=l-1; i>=0; i--){
            dynamic[i] = questions[i][0] + (i+1+questions[i][1] <l? dynamic[i+1+questions[i][1]] : 0);
            if(i<l-1)
                dynamic[i] = max(dynamic[i] , dynamic[i+1]);
        }
        return dynamic[0];
    }
};
