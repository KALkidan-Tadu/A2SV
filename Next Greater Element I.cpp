class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int i=0;
        vector<int> answer(nums1.size());
        while(i<nums1.size()){
            int j=0;
            while(j<nums2.size()){
                if(nums1[i]==nums2[j]){
                    while(nums1[i]>=nums2[j] && j<nums2.size()-1)
                        j++;
                    if(j<nums2.size() && nums2[j]>nums1[i]){
                        answer[i] = nums2[j];
                        break;
                    }  
                    else{
                        answer[i] = -1;
                        break;
                    }    
                }
                else
                    j++;
            }
            i++;
        }
        return answer;
    }
};
