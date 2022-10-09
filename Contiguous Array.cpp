class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int index=0, count=0, maxlen=0;
        unordered_map<int, int> mymap;
        mymap[0] = -1;
        while(index<nums.size()){
            if(nums[index]==0)
                count--;
            else
                count++;
            if(mymap.find(count)!=mymap.end())
                maxlen = max(maxlen, index-mymap[count]);
            else
                mymap[count] = index;
            index++;
        }
        return maxlen;
    }
};
