#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<int> g[5001]; 
int red[5001];
bool ok = false;
void addEdge(int a, int b){
    g[a].push_back(b);
    g[b].push_back(a);
}
void BFS(int v){
    vector<int> visited(5001, 0);
    vector<int> dist(5001, 0);
    queue<int> q;
    q.push(v);
    dist[v] = 0;
    visited[v] = 1;
    while(!q.empty()){
        int u = q.front();
        q.pop();
        if(red[u] == 1){
            cout << dist[u] << endl;
            return;
        }
        for(int h : g[u]){
            if(!visited[h]){
                visited[h] = 1;
                dist[h] = dist[u] + 1; 
                q.push(h);
            }
        }
    }
cout << -1 << endl;
}

int main(){
    int a;
    int b;
    int n;
    int m;
    int q;
    cin >> n >> m >> q;
    for(int i = 0; i < m; i++){
        cin >> a >> b;
        addEdge(a,b);
    }
    for(int i = 0; i < q; i++){
        cin >> a >> b;
        if(a == 1){
            red[b] = 1;
            ok = true;
        }
        else{
            if(!ok){
                cout << -1 << endl;
            }
            else{
                BFS(b);
            }
        }
    }    
}