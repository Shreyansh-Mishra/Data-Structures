#include<bits/stdc++.h>
using namespace std;
class Graph{
long long int V;
list<long long int>adj[4];
public:


void addEdge(long long int a, long long int b){
adj[a].push_back(b);
}

void dfsutil(long long int v,bool visited[]){
visited[v]=true;
cout<<v<<" ";
list<long long int>::iterator i;
for(i=adj[v].begin();i!=adj[v].end();i++){
    if(!visited[*i]){
        dfsutil(*i,visited);
    }
}

}
void dfs(long long int v,long long int size){
    bool V[size];
    for(int i=0;i<size;i++){
        V[i]=false;
    }
    dfsutil(v,V);
}
};

int main(){
    Graph g1;
    g1.addEdge(0,1);
    g1.addEdge(0,2);
    g1.addEdge(1,2);
    g1.addEdge(2,0);
    g1.addEdge(2,3);
    g1.addEdge(3,3);
    g1.dfs(2,4);


}