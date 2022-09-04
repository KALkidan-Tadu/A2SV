class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> answer;
        int a = matrix.size();
        int b = matrix[0].size();
        int total = a*b;
        int rt= b-1, rb= a-1, lb=0, lt=1;
        int i=0, j=0;
        while(total>0){
            while(j<=rt && total>0){
                answer.push_back(matrix[i][j]);
                j++;
                total--;
            }i++;
            j--;
            if(total==0)
                break;
            while(i<=rb && total>0){
                answer.push_back(matrix[i][j]);
                i++;
                total--;
            }j--;
            i--;
            if(total==0)
                break;
            while(j>=lb && total>0){
                answer.push_back(matrix[i][j]);
                j--;
                total--;
            }i--;
            j++;
            if(total==0)
                break;
            while(i>=lt && total>0){
                answer.push_back(matrix[i][j]);
                i--;
                total--;
            }j++;
            i++;
            rt--;
            rb--;
            lb++;
            lt++;
        }
        return answer;
    }
};
