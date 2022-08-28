class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* start = new ListNode;
        start->val = -1;
        ListNode* answer = NULL;
        int carry = 0;
        while(l1 != NULL && l2 != NULL){
            int sum = l1->val + l2->val;
             if(start->val == -1)
                {
                    ListNode *temp = new ListNode;
                    temp->val = (sum + carry)% 10;
                    temp->next = NULL;
                    start = temp;
                    answer = temp;
                }
                else
                {
                    ListNode *temp = new ListNode;
                    temp->val = (sum + carry)% 10;
                    temp->next = NULL;
                    start->next = temp;
                    start = temp;
                }
            if(sum+carry >= 10)
                carry = 1;
            else
                carry = 0;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1 != NULL){
             int sum = l1->val;
             ListNode *temp = new ListNode;
             temp->val = (sum + carry)%10;
             temp->next = NULL;
             start->next = temp;
             start = temp;
             l1 = l1->next; 
            if(sum+carry >= 10)
                 carry= 1;
            else
                carry = 0;
        }
        while(l2 != NULL){
             int sum = l2->val;
             ListNode *temp = new ListNode;
             temp->val = (sum + carry)%10;
             temp->next = NULL;
             start->next = temp;
             start = temp;
             l2 = l2->next;
             if(sum+carry >= 10)
                 carry= 1;
            else
                carry = 0;
        }
        if(carry==1){
             ListNode *temp = new ListNode;
             temp->val = 1;
             temp->next = NULL;
             start->next = temp;
             start = temp;
        }
            
        return answer;
    }
};
