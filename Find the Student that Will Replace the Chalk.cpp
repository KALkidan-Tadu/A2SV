class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long sum = 0;
        int index = 0;
       for(int i=0; i<chalk.size(); i++)
           sum += chalk[i];
        k%=sum;
        for(int i=0; i<chalk.size(); i++){
            if(k<chalk[i]){
                index = i;
                break;
            }
            else
                k -= chalk[i];
        }
        return index;
    }
};
