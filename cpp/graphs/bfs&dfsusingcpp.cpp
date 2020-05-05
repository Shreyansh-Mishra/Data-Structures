#include<bits/stdc++.h>
using namespace std;
class Graph{
    int v;
    list<int>*adj;
    public:
        Graph(int v){
            this->v=v;
            adj= new list<int>[v];
        }

        
        void addEdge(int a,int b){
            adj[a].push_back(b);
        }

        void bfs(int v,int size){
            bool v1[size];
            for(int i=0;i<size;i++){
                v1[i]=false;
            }
            v1[v]=true;
            list<int>queue;
            list<int>::iterator i;

            queue.push_back(v);
            while(!queue.empty()){
                int s=queue.front();
                cout<<s<<" ";
                queue.pop_front();
                for(i=adj[s].begin();i!=adj[s].end();i++){
                    if(!v1[*i]){
                        v1[*i]=true;
                        queue.push_back(*i);
                    }
                }

            }
        }
    void dfsutil(int v,bool v2[]){
        v2[v]=true;
        cout<<v<<" ";
        list<int>::iterator i;
        for(i=adj[v].begin();i!=adj[v].end();i++){
            if(!(v2[*i])){
                dfsutil(*i,v2);
            }
        }

    }    
    void dfs(int v,int size){
        bool v2[size];
        for(int i=0;i<size;i++){
            v2[i]=false;
        }
        dfsutil(v,v2);
    }


};

int main(){
 Graph g(4);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(2,0);
    g.addEdge(2,3);
    g.addEdge(3,3);
    cout<<"BFS: ";
    g.bfs(2,4);
    cout<<endl;
    cout<<"DFS: ";
    g.dfs(2,4);
    cout<<endl;
}