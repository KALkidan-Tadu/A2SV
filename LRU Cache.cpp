class LRUCache {
public:
    struct ListNode{
       int val;
       int key;
       ListNode* next;
       ListNode* prev;
    };
    ListNode* head = NULL;
    ListNode* tail = NULL;
    int size;
    unordered_map<int, ListNode*>mymap;
    void pushtoend(ListNode* temp){
        if(head==tail || temp==tail)
            return;
        if(temp == head){
            head = head->next;
            head->prev = NULL;
            temp->next = NULL;
            temp->prev = tail;
            tail->next = temp;
            tail = temp;
        }else{
            temp->next->prev = temp->prev;
            temp->prev->next = temp->next;
            temp->next = NULL;
            temp->prev = tail;
            tail->next = temp;
            tail = temp;
        }
    }
    void insertNode(int key, int value){
       if(head==NULL){
           ListNode* temp = new ListNode;
           temp->val = value;
           temp->key = key;
           temp->next = NULL;
           temp->prev = NULL;
           head = temp;
           tail = temp;
       } else{
           ListNode* temp = new ListNode;
           temp->val = value;
           temp->key = key;
           temp -> next = NULL;
           tail -> next = temp;
           temp -> prev = tail;
           tail = temp;
       }
        mymap[key] = tail;
    }
    void deleteNode(ListNode* temp, int key){
         if(temp == head){
            if(head->next != NULL){
                head = head->next;
                head->prev = NULL;
            }
            else{
                head = NULL;
                tail = NULL;
            } 
        }else if(temp == tail){
            tail->prev->next = NULL;
            tail = temp->prev;
        }else{
            temp->prev->next = temp->next;
            temp->next->prev = temp->prev;
        }
        delete temp;
        mymap.erase(key);
    }
    LRUCache(int capacity) {
        size = capacity;
    }
    
    int get(int key) {
        if(mymap.find(key) == mymap.end())
            return -1;
        ListNode* temp = mymap[key];
        pushtoend(temp);
        return temp->val;
    }
    void put(int key, int value) {
        if(mymap.find(key) == mymap.end()){
            if(size>0){
               insertNode(key, value);
               size--;
            }else{
                deleteNode(head, head->key);
                insertNode(key, value);
            }
        }else{
            ListNode* temp = mymap[key];
            deleteNode(temp, temp->key);
            insertNode(key, value);
        }
    }
};
