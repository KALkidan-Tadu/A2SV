class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> answer;
        vector<int> sub;
        for(int i=0; i<l.size(); i++){
          for(int j=l[i]; j<=r[i]; j++){
              sub.push_back(nums[j]);
          }  
            sort(sub.begin(), sub.end(), greater <>());
            bool equal = true;
            int diff = sub[0] - sub [1];
            for(int i=2; i<sub.size(); i++){
                if(sub[i-1] - sub[i] != diff){
                    equal = false;
                    break;
                }
            }
            if(equal)
                answer.push_back(true);
            else
                answer.push_back(false);
            sub.clear();
        }
        return answer;
    }
};
