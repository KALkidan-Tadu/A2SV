class MyQueue {
public:
    stack<int> stack1;
    stack<int> stack2;
    MyQueue() {
    }
    
    void push(int x) {
       while(!stack1.empty()){
           int k = stack1.top();
           stack1.pop();
           stack2.push(k);
       }
        stack1.push(x);
        while(!stack2.empty()){
           int k = stack2.top();
           stack2.pop();
           stack1.push(k);
       }
    }
    
    int pop() {
        int num = stack1.top();
        stack1.pop();
        return num;
    }
    
    int peek() {
        return stack1.top();
    }
    
    bool empty() {
        if(stack1.empty())
            return true;
        return false;
    }
};
