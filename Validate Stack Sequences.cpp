class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int i=0, j=0;
        stack<int> stack;
        while(j<popped.size()){
            if(i<popped.size() && pushed[i]==popped[j]){
                i++;
                j++;
            }else if(i<pushed.size()){
                if(!stack.empty() && stack.top()==popped[j]){
                    stack.pop();
                    j++;
                }else{
                   stack.push(pushed[i]);
                   i++; 
                }
                 }
            else{
                if(stack.top()==popped[j]){
                    stack.pop();
                    j++;
                }else
                    return false;
            }
        }
        if(stack.empty())
            return true;
        return false;
    }
};
