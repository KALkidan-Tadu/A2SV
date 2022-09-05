class NumMatrix {
public:
    vector<int> sums;
    vector<vector<int>> nums;
    NumMatrix(vector<vector<int>>& matrix) {
        nums = matrix;
        int a = nums.size(); 
        int b = nums[0].size();
        for(int i = 0; i<a; i++){
           sums.push_back(nums[i][0]);
            for(int j=1; j<b; j++){
                sums.push_back(sums.back() + nums[i][j]);
            }
        }
    }
    int sumRegion(int row1, int col1, int row2, int col2) {
        int a = nums.size();
        int b = nums[0].size();
        int answer = 0;
        int r = row1;
        while(r<=row2){
            answer += sums[(r*b)+col2] - ((col1>0)? sums[(r*b)+(col1-1)] : 0);
            r++;
        }
        return answer;
    }
};
