class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int sum = 0 , left = 0, right = cardPoints.size()-1, answer=0;
        while(left < k)
            sum += cardPoints[left++];
        answer = sum;
        left--;
        while(left>=0){
            sum = sum - cardPoints[left--] + cardPoints[right--];
            answer = max(answer, sum);
        }
        return answer;
    }
};
