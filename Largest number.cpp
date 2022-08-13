class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string answer; 
        bool zero = true;
        vector<string> str;
         for(int i=0; i<nums.size(); i++){
            if(nums[i] != 0){
                zero = false;
                break;
            }
        }
        if(zero)
            return "0";
        for(int i=0; i<nums.size(); i++){
            string temp = to_string(nums[i]);
            str.push_back(temp);
        }
        for (int i = 0; i < str.size()- 1; i++){
            for (int j = 0; j < str.size() - i - 1; j++){
                        if(str[j]+str[j+1] <str[j+1]+str[j]){
                            string temp = str[j];
                            str[j] = str [j+1];
                            str[j+1] = temp;
                        }
            }
        }
        for(int i=0; i< str.size(); i++){
            answer = answer + str[i];
        }
                    return answer;
    }
};
