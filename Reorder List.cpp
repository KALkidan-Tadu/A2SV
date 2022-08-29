class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* temp = head;
        vector<ListNode*> lists;
        while(temp != NULL){
            lists.push_back(temp);
            temp = temp->next;
        }
        int i=0, j=lists.size()-1;
        while(i<j){
            lists[i]->next = lists[j];
            i++;
            lists[j]->next = lists[i];
            j--;
            if(i==lists.size()/2){
                lists[i]->next = NULL;
                break;
            }
            if(j==lists.size()/2){
                lists[j]->next = NULL;
                break;
            }
        }
    }
};
