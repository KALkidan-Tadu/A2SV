class Solution {
public:
    string decodeString(string s) {
        int i=0, count=0;
        string result="";
        string digit="";
        stack<int> nums;
        stack<string> words;
        while(i<s.length()){
            if(isdigit(s[i])){
               while(isdigit(s[i])){
                digit=digit+s[i];    
                i++; 
                }
               nums.push(stoi(digit));
                digit = "";
            }if(s[i]==']'){
                count--;
                string answer="";
                while(words.top()!="["){
                    answer = words.top() + answer;
                    words.pop();
                }words.pop();
                int k = nums.top();
                nums.pop();
                string one = answer;
                while(k>1){
                    answer = answer + one;
                    k--;
                }
                if(count==0 && words.empty())
                    result = result+answer;
                else
                    words.push(answer);
                i++;
        }
            else{
                if(s[i]=='[')
                    count++;
                string c="";
                c = c+s[i];
                words.push(c);
                i++;
            }
        }
        while(!nums.empty()){
            string answer="";
                while(words.top()!="["){
                    answer = words.top() + answer;
                    words.pop();
                }
                words.pop();
                int k = nums.top();
                nums.pop();
                string one= answer;
                while(k>1){
                    answer = answer + one;
                    k--;
                }
                if(count==0 && words.empty())
                    result = result+answer;
                else
                    words.push(answer);
        }   
            if(words.empty())
                return result;
             string answer = "";
             while(!words.empty()){
                 answer = words.top()+answer;
                 words.pop();
             }
        return result+answer;
    }
};
