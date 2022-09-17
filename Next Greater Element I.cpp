class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> mymap;
        stack<int> mystack;
        for(int i=0; i<nums2.size(); i++){
            if(mystack.empty() || mystack.top()>=nums2[i])
                mystack.push(nums2[i]);
            else{
                while(!mystack.empty() && mystack.top()<nums2[i]){
                    int n = mystack.top();
                    mymap[n] = nums2[i];
                    mystack.pop();
                }
                mystack.push(nums2[i]);
            }
            }
        while(!mystack.empty()){
                int n = mystack.top();
                mymap[n] = -1;
                mystack.pop();
        }
        for(int i=0; i<nums1.size(); i++){
            nums1[i] = mymap[nums1[i]];
        }
        return nums1;
    }
};


/*class Solution {
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
*/
