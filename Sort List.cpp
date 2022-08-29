class Solution {
public:
    ListNode* sortList(ListNode* head) {
        vector<int>list;
        ListNode* temp = head;
        while(temp != NULL){
            list.push_back(temp->val);
            temp = temp->next;
        }
        sort(list.begin(), list.end());
        int i = 0;
        temp = head;
        while(i<list.size()){
            temp->val = list[i];
            temp = temp->next;
            i++;
        }
        return head;
    }
};
