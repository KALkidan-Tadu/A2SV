class MinStack {
public:
    vector<int> stack; 
    vector<int> minS;
    int size;
    MinStack() {
        size = 0;
        minS.push_back(INT_MAX);
    }
    void push(int val) {
        stack.push_back(val);
        minS.push_back(min(minS[size],val));
        size++;
    }
    
    void pop() {
        stack.pop_back();
        minS.pop_back();
        size--;
    }
    
    int top() {
        return stack[size-1];
    }
    
    int getMin() {
        return minS[size];
    }
};


/*class MinStack {
public:
    vector<int>* stack; 
    vector<int> min;
    MinStack() {
      stack = new vector<int>;
    }
    void push(int val) {
        stack->push_back(val);
        min.push_back(val);
    }
    
    void pop() {
        stack->pop_back();
        min.pop_back();
    }
    
    int top() {
        int n = min.size()-1;
        return min[n];
    }
    
    int getMin() {
        int m = min[0];
        for(int i=1; i<min.size(); i++){
            if(min[i]<m)
                m = min[i];
        }
        return m;
    }
};
*/
