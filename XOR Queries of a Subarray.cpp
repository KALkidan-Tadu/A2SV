class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> answer(queries.size());
        for(int i=1; i<arr.size(); i++)
            arr[i] = arr[i] ^ arr[i-1];
        for(int i=0; i<queries.size(); i++){
            int a = queries[i][0];
            int b = queries[i][1];
            if(a==0)
                answer[i] = arr[b];
            else
                answer[i] = arr[a-1] ^ arr[b];
        }
        return answer;
    }
};
