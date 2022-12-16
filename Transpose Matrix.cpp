class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        vector<vector<int>> matrixT(m);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++)
                matrixT[j].push_back({matrix[i][j]});
        }
        return matrixT;
    }
};
