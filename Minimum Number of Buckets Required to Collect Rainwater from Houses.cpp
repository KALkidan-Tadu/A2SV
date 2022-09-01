class Solution {
public:
    int minimumBuckets(string street) {
        int bucket = 0;
        int i=0;
        if(street.length()==1 && street[0]=='H')
            return -1;
        while(i<street.length()){
            while(i<street.length() && street[i]!='H'){
                i++;
            }
            if(i>=street.length())
                break;
            if(i>0 && i<street.length()-1 && street[i-1] == 'H' && street[i+1] == 'H')
                return -1;
            if((i==0 && street[i+1]=='H') || (i==street.length()-1 && street[i-1]=='H'))
                return -1;
            if(i==0 && street[i+1] == '.'){
                street[i+1] = 'B';
                bucket ++;
            }else if(i==street.length()-1 && street[i-1]=='.'){
                street[i-1] = 'B';
                bucket ++;
            }
            else if(i<street.length()-1 && street[i-1]=='.' && street[i+1]=='.'){
                street[i+1] = 'B';
                bucket ++;
            }
            else if(i<street.length()-1 && street[i+1]=='.' && street[i-1]!='B'){
                street[i+1] = 'B';
                bucket ++;
            }
            else if(i<street.length()-1 && street[i-1]=='.'){
                street[i-1] = 'B';
                bucket ++;
            }
            i++;
        }
        return bucket;
    }
};
