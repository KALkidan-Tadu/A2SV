class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(n--){
            fast = fast->next;
        }
        if(fast==NULL){
            return slow->next;
        }else{
            while(fast->next){
                slow = slow->next;
                fast = fast->next;
            }
            slow->next = slow->next->next;
            return head;
        }
    }
};
