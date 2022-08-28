class Solution {
public:
    int pairSum(ListNode* head) {
        int max = 0;
        ListNode *sgl = head;
        ListNode *dbl = head;
        while(dbl!=NULL){
            dbl = dbl->next->next;
            sgl = sgl->next;
        }
        ListNode *secondhalf = reverseList(sgl);
        ListNode *second = secondhalf;
        dbl = head;
        while(second != NULL){
            int sum = dbl->val + second->val;
            if(sum > max)
                max = sum;
            dbl = dbl->next;
            second = second->next;
        }
        return max;
    }
    ListNode* reverseList(ListNode *h){
        if(h == NULL)
            return 0;
        if(!h->next || !h)
            return h;
        auto answer = reverseList(h->next);
        h->next->next = h;
        h->next = NULL;
        return answer;
        }
};
