class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int score = 0, left=0, right=tokens.size()-1, answer=0;
        sort(tokens.begin(), tokens.end());
        while(left<=right && (power>=tokens[left] || score>0)){
            while(left<=right && power>=tokens[left]){
                score++;
                power -= tokens[left++];
            }
            answer = max(answer, score);
            if(left<=right && score>0){
                score--;
                power += tokens[right--];
            }
        }
        return answer;
    }
};
