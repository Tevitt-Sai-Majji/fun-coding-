#include <iostream>
#include<bits/stdc++.h>

using namespace std;
vector<int>add(vector<int>&x,vector<int>&y){
  reverse(x.begin(),x.end());
  reverse(y.begin(),y.end());
  long long int len=min(x.size(),y.size());
  int carry=0;
  vector<int>ans;
  for(int i=0;i<len;i++){
    int val=x[i]+y[i]+carry;
    carry=val/10;
    ans.push_back(val%10);
  }
  if(x.size()>len){
    for(int i=len;i<x.size();i++){
      int val=x[i]+carry;
      carry=val/10;
      ans.push_back(val%10);
    }
  }
  if(y.size()>len){
    for(int i=len;i<y.size();i++){
      int val=y[i]+carry;
      carry=val/10;
      ans.push_back(val%10);
    }
  }
  if(carry>0){
    ans.push_back(carry);
  }
  reverse(ans.begin(),ans.end());
  return ans;
}

int main() {
  long long int t;
  cin>>t;
  while(t--){
    string a,b;
    cin>>a>>b;//a='12345678' b="87654323"
    vector<int>va;
    vector<int>vb;
    for(int i=0;i<a.size();i++){
      va.push_back(a[i]-'0');
    }
    for(int i=0;i<b.size();i++){
      vb.push_back(b[i]-'0');
    }
    vector<int>sum=add(va,vb);
    for(auto i:sum){
      cout<<i;
    }
    cout<<"\n";
  }
  return 0;
}
