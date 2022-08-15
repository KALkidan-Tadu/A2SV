class Solution {
public:
    int minSetSize(vector<int>& arr) {
        vector<int> freq;
        int count = 1;
        sort(arr.begin(), arr.end());
        for(int i=1; i<arr.size(); i++){
             if(arr[i] == arr[i-1])
                 count++;
            else{
                freq.push_back(count);
                count = 1;
            }            
        }
        freq.push_back(count);
        sort(freq.begin(), freq.end(), greater<>());
        int answer=0, sum=0;
          while(sum < arr.size()/2){
            sum += freq[answer++];
        }  
        return answer;
    }
};
