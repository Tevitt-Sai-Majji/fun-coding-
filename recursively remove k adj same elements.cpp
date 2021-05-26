#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    string rec(string s,string prev,int k){
        if(s.size()<2 || s==prev) return s;
        string res="";
        int i=0,n=s.size();
        while(i<n){
            if(i==n-1 and s[i]!=s[i-1] and k>1) res+=s[i++];
            else if(i+1<n and s[i]!=s[i+1] and k>1) res+=s[i++];
            else{
                int count=0;
                while(i+1<n and s[i]==s[i+1]){
                    i++;
                    count++;
                  }
                i++;
                for(int j=0;j<(count+1)%k;j++)res+=s[i-1];
                //res+=(s[i-1]*(count)%k);
            }
        }
        prev=s;
        s=res;
        return rec(s,prev,k);
    }
    string Reduced_String(int k,string s){
        return rec(s,"",k);
    }
};
int main() { 
    int t;cin>>t;
    while(t--)
    {
        int k;
        cin>>k;
        string s;
        cin>>s;
        Solution obj;
        cout<<obj.Reduced_String(k,s)<<"\n";  
    }
	return 0;
}
