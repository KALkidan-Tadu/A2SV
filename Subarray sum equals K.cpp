class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> sumMap;
        int sum=0, i=0, count=0;
        while(i<nums.size()){
            sum+=nums[i];
            if(sum==k)
                count++;
            if(sumMap.find(sum-k)!=sumMap.end())
                count+= sumMap[sum-k];
            sumMap[sum]+=1;
            i++;
        }
        return count;
    }
};
