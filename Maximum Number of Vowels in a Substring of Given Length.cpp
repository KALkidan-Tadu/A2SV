class Solution {
public:
    int maxVowels(string s, int k) {
        int left = 0 , right = 0;
        long vowel = 0;
        while(right<k){
            if(isVowel(s[right]))
                vowel++;
            right++;
        }
        long answer = vowel;
        while(right<s.length()){
            if(isVowel(s[left]))
                vowel--;
            left++;
            if(isVowel(s[right]))
                vowel++;
            right++;
            answer = max(answer, vowel);
        }
        return answer;
    }
    bool isVowel(char ch){
        if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
            return true;
        return false;
    }
};
