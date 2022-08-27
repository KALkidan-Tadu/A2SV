bool has_cycle(SinglyLinkedListNode* head) {
    if(head == NULL)
       return 0;
    unordered_map<SinglyLinkedListNode*, int> myMap;
    bool loop = false;
      SinglyLinkedListNode *temp = head;
      while(temp != NULL){
          if(myMap[temp] >0){
              loop = true;
              break;
          }else{
              myMap[temp] ++;
              temp = temp->next;
          }
      }
    if(loop==true){
        return true;
    }
    return false;
}
