class MinStack {
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
