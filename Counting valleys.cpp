int countingValleys(int steps, string path) {
    int answer=0, count=0;
    bool down;
    for(int i=0; i<steps; i++){
        if(count<=0 && path[i]=='D'){
            count--;
            down = true;
        }else if(count<0 && path[i]=='U'){
            count++;
            down = true;
        }else if(count>=0 && path[i]=='U'){
            count++;
            down = false;
        }else{
            count--;
            down = false;
        }
        if(count==0 && down){
            answer++;
        }
    }
    return answer;
    }
