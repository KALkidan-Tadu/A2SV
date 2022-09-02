class Solution {
public:
    int totalFruit(vector<int>& fruits) {
       int lastfruit = -1, secondlast = -1;
        int lastcount=0, currmax=0, maxf=0;
        for(int fruit : fruits)
       {
          if(fruit==lastfruit || fruit==secondlast)
              currmax+=1;
            else
                currmax = lastcount+1;
            if(fruit==lastfruit)
                lastcount+=1;
            else
                lastcount = 1;
            if(fruit!=lastfruit){
                secondlast = lastfruit;
                lastfruit  = fruit;
            }
            maxf = max(currmax,maxf);
      }
        return maxf;
    }
};
