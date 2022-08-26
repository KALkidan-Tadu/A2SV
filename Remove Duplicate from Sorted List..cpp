class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL)
            return 0;
        if(!head || !head->next)
            return head;
        ListNode *root1 = head;
        ListNode *root2 = head->next;
        while(root2 != NULL){
            if(root1->val == root2->val){
                root1->next = root2->next;
                delete root2;
                root2 = root1->next;
            }
            else{
                root1 = root2;
                root2 = root1->next;
            }
        }
        return head;
    }
};
