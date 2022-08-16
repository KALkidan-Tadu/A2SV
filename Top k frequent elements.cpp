class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<int> answer;
        vector<vector<int>> freq(nums.size(),vector<int>(2,0));
        int count =1, m=0, i;
          for(i=1; i<nums.size(); i++){
             if(nums[i] == nums[i-1])
                 count++;
            else{
                freq[m][0] = count;
                freq[m][1] = i-1;
                m++;
                count = 1;
            }            
        }
        freq[m][0] = count;
        freq[m][1] = i-1;
        sort(freq.begin(), freq.end(), greater<>());
        for(int i=0; i<k; i++){
            int n = freq[i][1];
            answer.push_back(nums[n]);
        }
        return answer;
    }
};
