class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int n=1;
        ListNode *temp = head;
        while(temp->next != NULL){
            temp = temp->next;
            n++;
            if(n%2 == 0)
                head = head->next;
        }
        return head;
    }
};
