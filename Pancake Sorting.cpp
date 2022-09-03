class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int>flips;
        int val = arr.size();
        while(val >=1){
          for(int i = 0; i<arr.size(); i++){
              if(arr[i]==val && i==val-1)
                  break;
              if(arr[i]==val && i==0){
                 flips.push_back(val);
                 reverse(arr.begin(), arr.begin()+val);
              }
            else if(arr[i] == val){
                flips.push_back(i+1);
                reverse(arr.begin(), arr.begin()+i+1);
                flips.push_back(val);
                reverse(arr.begin(), arr.begin()+val);
            }
        }  
            val--;
        }
        return flips;
    }
};
