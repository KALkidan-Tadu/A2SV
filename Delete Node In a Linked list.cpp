class Solution {
public:
    void deleteNode(ListNode* node) {
      ListNode *root = node;
      while(true){
          if(root->next->next == NULL){
              root->val = root->next->val;
              delete root->next;
              root->next = NULL;
              break;
          }
          root->val = root->next->val;
          root = root->next;
      }
    }
};
