class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        unordered_map<int,int> mymap;
        int answer = 0, currsum=0;
        mymap[0]=1;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]%2==0)
                currsum+=0;
            else
                currsum+=1;
            int diff = currsum-k;
            if(mymap.find(diff) != mymap.end())
                answer += mymap[diff];
            mymap[currsum]++;    
        }
        return answer;
    }
};
