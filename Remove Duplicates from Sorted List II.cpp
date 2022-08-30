class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL)
            return 0;
        if(!head || !head->next)
            return head;
        ListNode *root1 = head;
        ListNode *root2 = head->next;
        ListNode *root3 = head;
        while(root2 != NULL){
            if(root1->val == root2->val){
               while(root2!=NULL && root1->val == root2->val ){
                root1->next = root2->next;
                delete root2;
                root2 = root1->next;
            }
                if(root1 == head){
                    head = head->next; 
                if(root2 == NULL)
                   break;
                }else{
                    root3->next = root2;
                    delete root1;
                    root1 = root2;
                    if(root2 == NULL)
                        break;
                    else
                        root2 = root1->next;
                    while(root3->next!=root1)
                      root3 = root3->next;
                }
            }
            else{
                root1 = root2;
                root2 = root1->next;
                while(root3->next!=root1)
                    root3 = root3->next;
            }
        }
        return head;
    }
};
