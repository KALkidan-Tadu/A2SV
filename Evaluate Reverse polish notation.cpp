class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long> stack;
        for(int i=0; i<tokens.size(); i++){
            if(tokens[i]=="+"){
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();
                stack.push(a+b);
            }
            else if(tokens[i]=="-"){
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();
                stack.push(a-b);
            }
            else if(tokens[i]=="*"){
                long b = stack.top();
                stack.pop();
                long a = stack.top();
                stack.pop();
                stack.push(a*b);
            }
            else if(tokens[i]=="/"){
                long b = stack.top();
                stack.pop();
                long a = stack.top();
                stack.pop();
                stack.push(a/b);
            }
            else
                stack.push(stoi(tokens[i]));
        }
        return stack.top();
    }
};


/*class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        if(tokens.size()==1)
            return stoi(tokens[0]);
        stack.push_back(stoi(tokens[0]));
        stack.push_back(stoi(tokens[1]));
        for(int i=2; i<tokens.size(); i++){
            if(tokens[i]=="+"){
                int n = stack.size()-1;
                int b= stack[n];
                int a = stack[n-1];
                stack.pop_back();
                stack.pop_back();
                stack.push_back(a+b);
            }
             else if(tokens[i]=="-"){
                int n = stack.size()-1;
                int b= stack[n];
                int a = stack[n-1];
                stack.pop_back();
                stack.pop_back();
                stack.push_back(a-b);
            }
            else if(tokens[i]=="*"){
                int n = stack.size()-1;
                int b= stack[n];
                int a = stack[n-1];
                stack.pop_back();
                stack.pop_back();
                stack.push_back(a*b);
            }
            else if(tokens[i]=="/"){
                int n = stack.size()-1;
                int b= stack[n];
                int a = stack[n-1];
                stack.pop_back();
                stack.pop_back();
                stack.push_back(a/b);
            }
            else{
               stack.push_back(stoi(tokens[i])); 
            }
        }
        return stack[0];
    }
};
*/
