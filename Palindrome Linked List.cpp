class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == NULL)
            return true;
        vector<int> nums;
        while(head != NULL){
            nums.push_back(head->val);
            head = head->next;
        }
        int left =0, right=nums.size()-1;
        while(left<=right){
            if(nums[left]!=nums[right])
                return false;
            left+=1;
            right-=1;
        }
        return true;
    }
};
