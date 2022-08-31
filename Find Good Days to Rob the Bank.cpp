class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        vector<int> answer;
        if(time>=security.size())
            return answer;
        vector<int> before(security.size());
        vector<int> after(security.size());
        before[0] = 0;
        after[security.size()-1] = 0;
        for(int i=1; i<security.size(); i++){
            if(security[i-1]>=security[i])
                before[i] = before[i-1]+1;
            else
                before[i] = 0;
            }
        for(int j=security.size()-2; j>=0; j--){
            if(security[j]<=security[j+1])
                after[j] = after[j+1]+1;
            else
                after[j] = 0;
        }
        for(int i=time; i<security.size()-time; i++){
            if(before[i]>=time && after[i]>=time)
                answer.push_back(i);
        }
        return answer;
    }
};
