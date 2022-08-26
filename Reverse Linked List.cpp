class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL)
            return 0;
        if(!head->next || !head)
            return head;
        auto answer = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return answer;
    }
};
