#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    scanf("%d", &N);
    vector<pair<int, int>> mosquito;
    vector<int> grid;
    for(int i=0; i<N; i++) {
        int te, tx;
        scanf("%d %d", &te, &tx);
        mosquito.push_back({te, tx});
        grid.push_back(te);
        grid.push_back(tx);
    }
    sort(grid.begin(), grid.end());
    grid.erase(unique(grid.begin(), grid.end()), grid.end());
    
    vector<int> cnt(grid.size());
    
    for(auto& i : mosquito) {
        cnt[lower_bound(grid.begin(), grid.end(), i.first) - grid.begin()]++;
        cnt[lower_bound(grid.begin(), grid.end(), i.second) - grid.begin()]--;
    }
    
    int ans=0, me=0, mx=0;
    
    for(int i=0; i<cnt.size(); i++) {
        if(i>0)
            cnt[i]+=cnt[i-1];
        if(cnt[i]>ans) {
            ans = cnt[i];
            me = i;
            mx = i+1;
        }
        else if(cnt[i]==ans && mx==i)
            mx++;
    }
    
    printf("%d\n%d %d\n", ans, grid[me], grid[mx]);
    
    return 0;
}
