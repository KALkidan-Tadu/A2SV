class Solution {
public:
    int calculate(string s) {
        if(s.length()==0)
            return 0;
       int currnumber=0, lastnumber=0, result=0;
        char sign = '+';
        for(int i=0; i<s.length(); i++){
            char currchar = s[i];
            if(isdigit(currchar)){
                currnumber = (currnumber * 10) + (currchar - '0');
            }
            if(!isdigit(currchar) && !iswspace(currchar) || i==s.length()-1){
                if(sign == '+' || sign =='-'){
                    result += lastnumber;
                    lastnumber = (sign=='+')? currnumber : -currnumber;
                }else if(sign == '*'){
                    lastnumber = lastnumber * currnumber;
                }else if(sign = '/')
                    lastnumber = lastnumber / currnumber;
                sign = currchar;
                currnumber = 0;
            }
        }
        result +=lastnumber;
        return result;
    }
};
