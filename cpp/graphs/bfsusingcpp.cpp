#include<bits/stdc++.h>
using namespace std;

class Graph{
    private:
    int u,v;
    public:
    addEdge(list<int> adj[], int a,int b){
        adj[a].push_back(b);
    return 1;
    }
};

bfs(list<int> adj[], int s,int v){
    bool visited[v];
    for(int i=0;i<v;i++){
        visited[i]=false;
    }
    list<int> queue;
    queue.push_back(s);
    visited[s]=true;
    list<int>:: iterator i;
    while(!queue.empty()){
        s=queue.front();
        queue.pop_front();
        cout<<s<<" ";
        for(i=adj[s].begin();i!=adj[s].end();i++){
            if(!visited[*i]){
                queue.push_back(*i);
                visited[*i]=true;
            }
        }
    }
return 1;
}


int main(){
list<int> adj[4];
Graph g;
g.addEdge(adj,0,1);
g.addEdge(adj,0,2);
g.addEdge(adj,0,3);
g.addEdge(adj,1,2);
g.addEdge(adj,1,3);
g.addEdge(adj,2,1);
g.addEdge(adj,3,1);
bfs(adj,2,4);
return 0;
}