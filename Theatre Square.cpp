#include <iostream>
using namespace std;
int main(){
  long long n, m, a, count=0;
  cin>>n;
  cin>>m;
  cin>>a;
  long long width = n/a;
  if(n%a > 0)
    width += 1;
  m -= a;
  long long height = 0;
  if(m>0){
    height = m/a;
    if(m%a > 0)
      height += 1;
  }
  cout<< (height*width)+width;
  return 0;
}
