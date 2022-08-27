class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> answer;
        ListNode *temp1 = head;
        ListNode *temp2 = head->next;
        while(temp1 != NULL){
            temp2 = temp1->next;
            while(temp2 != NULL){
                if(temp2->val > temp1->val){
                    answer.push_back(temp2->val);
                    break;
                }
                if(temp2->next == NULL)
                    answer.push_back(0);
                temp2 = temp2->next;
            }
            if(temp1->next == NULL)
                    answer.push_back(0);
            temp1 = temp1->next;
        }
        return answer;
    }
};
