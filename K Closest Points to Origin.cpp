class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>> points, int k) {
        vector<vector<int>> answer(k,vector<int>(2,0));
        vector<vector<double>> temp(points.size(),vector<double>(2,0));
        int min;
        double distance;
        for(int i=0; i<points.size(); i++){
            for(int j=0; j<1; j++){
                distance = sqrt(pow(points[i][j],2)+ pow(points[i][j+1],2));
                temp[i][0] = distance;
                temp[i][1] = i;
            }
        }
        sort(temp.begin(), temp.end());
        for(int i=0; i<k; i++){
            int index = temp[i][1];
            answer[i][0] = points[index][0];
            answer[i][1] = points[index][1];
        }
        return answer;
    }
};
