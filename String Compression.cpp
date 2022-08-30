class Solution {
public:
    int compress(vector<char>& chars) {
        int i=0, count=1, j=0;
        while(i<chars.size() && j<chars.size()){
            count = 1;
            while(j<chars.size()-1 && chars[j+1] == chars[i]){
                j++;
                count++;
            }
            if(count>=1000){
                while(j>i+4){
                    chars.erase(chars.begin()+j);
                     j--;
                }
            }else if(count>=100){
                while(j>i+3){
                    chars.erase(chars.begin()+j);
                     j--;
                }
            }else if(count>=10){
                while(j>i+2){
                    chars.erase(chars.begin()+j);
                     j--;
                }
            }
            else{
                while(j > i+1){
                chars.erase(chars.begin()+j);
                j--;
            }
            }
            if(count>1){
                if(count>=1000){
                    chars[j-3] = char(count/1000)+'0';
                    chars[j-2] = char((count%1000)/100)+'0';
                    chars[j-1] = char(((count%1000)%100)/10)+'0';
                    chars[j] = char(count%10)+'0';
                }else if(count>=100){
                    chars[j-2] = char(count/100)+'0';
                    chars[j-1] = char((count%100)/10)+'0';
                    chars[j] = char(count%10)+'0';
                }
                else if(count>=10){
                    int q = count/10;
                    int r = count%10;
                    chars[j-1] = char(q)+'0';
                    chars[j] = char(r)+'0';
                }
                else{
                    chars[j] = char(count) + '0';
                    count = 1;
                }
            }
            j++;
            i = j;
        }
        return chars.size();
    }
};
