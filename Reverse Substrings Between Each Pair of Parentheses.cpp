class Solution {
public:
    string reverseParentheses(string s) {
        string answer, reversed;
        int n=0;
        stack<char> stack;
        for(int i=0; i<s.length(); i++){
            if(s[i]==')'){
                n--;
                while(stack.top()!='('){
                answer = answer + stack.top();
                stack.pop();
            }
                stack.pop();
                for(int j=0; j<answer.length(); j++){
                    stack.push(answer[j]);  
                }
                if(n==0){
                     reversed = reversed+answer;
                }
               
                if(i!=s.length()-1){
                    answer = "";
                }
            }
            else if(s[i]=='('){
                n++;
                stack.push(s[i]);
            }
            else
                if(n==0){
                    reversed= reversed+s[i];
                }else
                    stack.push(s[i]);
            }
        return reversed;
    }
};
