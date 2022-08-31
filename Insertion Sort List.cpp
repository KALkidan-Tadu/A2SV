class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* first = head->next;
        while(first != NULL){
            ListNode* sorted = head;
            while(sorted != NULL){
               if(first->val < sorted->val){
                int temp = first->val;
                first->val = sorted->val;
                sorted->val = temp;
            }
                sorted = sorted->next;
            }
            first = first->next;   
        }
        return head;
    }
};
