class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stack;
        if(k == num.length())
            return "0";
        for(int i=0; i<num.length(); i++){
            while(!stack.empty() && stack.top()> num[i] && k>0){
                stack.pop();
                k--;
            }
            if (!stack.empty() || num[i] != '0')
                stack.push(num[i]);
        }
            while(!stack.empty() && k>0){
                stack.pop();
                k--;
            }
        if (stack.empty())
            return "0";
        int l = num.length();
        while (!stack.empty())
        {
            num[l- 1] = stack.top();
            stack.pop();
            l-=1;
        }
        return num.substr(l);
    }
};
