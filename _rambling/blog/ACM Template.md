# ACM Template







## 数据范围

| 类型               | 最小值               | 最大值                          |
| ------------------ | -------------------- | ------------------------------- |
| unsigned int       | 0                    | 4294967295 (2^32 - 1)           |
| int                | -2147483648          | 2147483647 (2^31 - 1)           |
| unsigned long      | 0                    | 4294967295 (2^32 - 1)           |
| long               | -2147483648          | 2147483647 (2^31 - 1)           |
| Unsigned long long | 0                    | 18446744073709551615 (2^64 - 1) |
| long long          | -9223372036854775808 | 9223372036854775807 (2^63 - 1)  |
| unsigned __int64   | 0                    | 18446744073709551615 (2^64 - 1) |
| __int64            | -9223372036854775808 | 9223372036854775807 (2^63 - 1)  |



```cpp
inline int read()
{
	char c = getchar();
	int x = 0;
	bool minus = 0;
	for (; !isdigit(c); c = getchar())
		if (c == '-')minus = 1;
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	if (minus)return -x;
	return x;
}
```



# 数论

### EXGCD

#### 题目描述

求关于x*x*的同余方程$ a x \equiv 1 \pmod {b} $的最小正整数解。

#### 输入格式

一行，包含两个正整数 a,b*a*,*b*，用一个空格隔开。

#### 输出格式

一个正整数 x_0*x*0，即最小正整数解。输入数据保证一定有解。

```cpp
#include <bits/stdc++.h>
#define ll long long
using namespace std;
int xs, ys;

ll Exgcd(ll a, ll b)
{
	if (b == 0)
	{
		xs = 1;
		ys = 0;
		return a;
	}
	ll k = Exgcd(b, a%b)
    ;
	ll t = xs;
	xs = ys;
	ys = t - (a / b)*ys;
	return k;
}

int main()
{
	ll a = 0, b = 0;
	cin >> a >> b;

	Exgcd(a, b);
	cout << (xs + b) % b;

    return 0;
}


```



# 数学杂项

## 最长公共子序列

### 题目描述

给出 1,2,\ldots,n1,2,…,*n* 的两个排列 P_1*P*1 和 P_2*P*2 ，求它们的最长公共子序列。

### 输入格式

第一行是一个数 n*n*。

接下来两行，每行为 n*n* 个数，为自然数 1,2,\ldots,n1,2,…,*n* 的一个排列。

### 输出格式

一个数，即最长公共子序列的长度。

```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn = 100005;
const int INF = 1 << 5;
int p1[maxn];
int a[maxn];
int b[maxn];

inline int read()
{
	char c = getchar(); int x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	return x;
}

int main()
{
	memset(b, INF, sizeof(b));
	int n = 0, ind = 0;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		p1[read()] = i;
	}
	for (int i = 1; i <= n; i++)
	{
		int x = p1[read()];
		*lower_bound(b+1,b+n+1,x)=x;
	}
	printf("%d", lower_bound(b + 1, b + n + 1, b[0]) - b - 1);
	return 0;
}
```



## 矩阵快速幂

```cpp
// P3390.cpp: 定义控制台应用程序的入口点。
//


#include <bits/stdc++.h>
#define ll long long 
using namespace std;

inline ll read()
{
	char c = getchar(); ll x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	return x;
}
ll n, k;
const ll mod = 1e9 + 7;
struct Matrix
{
	ll _[105][105];
	Matrix()
	{
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				this->_[i][j] = 0;
	}
	Matrix operator* (const Matrix& A)const
	{
		Matrix z;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				for (int l = 1; l <= n; l++)
					z._[i][j] = (z._[i][j] % mod + ((this->_[i][l]) % mod * (A._[l][j]) % mod) % mod) % mod;
		return z;
	}
};
Matrix T;
inline void print(Matrix& A)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			printf("%lld ", A._[i][j] % mod); 
		printf("\n");
	}
}

inline void getM(Matrix& A)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			A._[i][j] = read();
	}
}

inline void Einit(Matrix& E)
{
	for (int i = 1; i <= n; i++)
	{
		E._[i][i] = 1;
	}
}

inline void pww(Matrix& S, ll k)
{
	while (k )
	{
		if (k & 1)
			S = S * T;
		T = T * T;
		k >>= 1;
	}
}

int main()
{
	cin >> n >> k;
	getM(T);
	Matrix E;
	Einit(E);
	pww(E, k);
	print(E);

	return 0;
}


```



## 高斯消元法

### 题目描述

给定一个线性方程组，对其求解

### 输入格式

第一行，一个正整数 n*n*

第二至 n+1*n*+1行，每行 n+1*n*+1 个整数，为a_1, a_2 \cdots a_n*a*1,*a*2⋯*a**n* 和 b*b*，代表一组方程。

### 输出格式

共n行，每行一个数，第 i*i*行为 x_i*x**i* （保留2位小数）

如果不存在唯一解，在第一行输出"No Solution".

```cpp
// P3389.cpp: 定义控制台应用程序的入口点。
//


#include <bits/stdc++.h>
#define dd double
#define b n+1
using namespace std;
dd a[300][300];
int n;
const dd eps = 1e-8;



int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		{
			for (int j = 1; j <= n + 1; j++)
				cin >> a[i][j];
		}
		for (int j = 1; j < i; j++)
		{
			if (fabs(a[j][b]) < fabs(a[i][b]))swap(a[j], a[i]);
		}
	}
	for (int i = 1; i <= n; i++)
	{
		if (fabs(a[i][i]) <= eps)
		{
			printf("No Solution\n");
			return 0;
		}
		//debug();
		for (int j = i+1; j <= b; j++)
			a[i][j] /= a[i][i];

		for (int j = 1; j <= n; j++)
			if (j != i)
				for (int k = i+1; k <= b; k++)
					a[j][k] -= a[i][k] * a[j][i];
	}
	//debug();
	for (int i = 1; i <= n; i++)printf("%.2lf\n", a[i][b]);
	return 0;
}


```



# 图论

## 最小生成树

### 题目描述

如题，给出一个无向图，求出最小生成树，如果该图不连通，则输出 `orz`。

### 输入格式

第一行包含两个整数 N,M*N*,*M*，表示该图共有 N*N* 个结点和 M*M* 条无向边。

接下来 M*M* 行每行包含三个整数 X_i,Y_i,Z_i*X**i*,*Y**i*,*Z**i*，表示有一条长度为 Z_i*Z**i* 的无向边连接结点 X_i,Y_i*X**i*,*Y**i*。

### 输出格式

如果该图连通，则输出一个整数表示最小生成树的各边的长度之和。如果该图不连通则输出 `orz`。

```cpp
//
//  main.cpp
//  MinGenTree
//
//  Created by CONIO on 2020/12/13.
//
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

inline int read()
{
    int x=0;char c=getchar();
    for(;!isdigit(c);c=getchar());
    for(;isdigit(c);c=getchar())
        x=x*10+c-'0';
    return x;
}

struct edge
{
    int u,v,w;
    edge(){}
    edge(int a,int b,int c)
    {
        u=a;
        v=b;
        w=c;
    }
    bool operator <(const edge e)const
    {
        return this->w<e.w;
    }
};

const int N=5005,M=200005;
edge e[M];
int n,m,FA[N];

void init()
{
    for(int i=1;i<=n;i++)
    {
        FA[i]=i;
    }
}

int find1(int x)
{
    if(FA[x]==x)return x;
    return FA[x]=find1(FA[x]);
}
queue<int> Q;
inline int find(int x)
{
    while(FA[x]!=x)
    {
        Q.push(x);
        x=FA[x];
    }
    while(!Q.empty())
    {
        FA[Q.front()]=x;
        Q.pop();
    }
    return x;
}

void join(int x,int y)
{
    int u=find(x);
    int v=find(y);
    FA[u]=v;
}


int main(int argc, const char * argv[]) {
    cin>>n>>m;
    init();
    for(int i=1;i<=m;i++)
    {
        int u=read();
        int v=read();
        int w=read();
        e[i]=edge(u,v,w);
    }
    sort(e+1, e+m+1);
    int sum=0,k=0;
    for(int i=1;i<=m;i++)
    {
        int u=e[i].u;
        int v=e[i].v;
        int w=e[i].w;
        if(find(u)!=find(v))
        {
            join(u,v);
            sum+=w;
            k++;
        }
        if(k==n-1)break;
    }
    if(k==n-1)cout<<sum;
    else cout<<"orz";
    //std::cout << "Hello, World!\n";
    return 0;
}

```



## 最近公共祖先（LCA）

### 输入格式

第一行包含三个正整数 N,M,S*N*,*M*,*S*，分别表示树的结点个数、询问的个数和树根结点的序号。

接下来 N-1*N*−1 行每行包含两个正整数 x*,*y*，表示 *x* 结点和 *y* 结点之间有一条直接连接的边（数据保证可以构成树）。

接下来 M*M* 行每行包含两个正整数 a*,*b*，表示询问 a*a* 结点和 b*b* 结点的最近公共祖先。

### 输出格式

输出包含 M*M* 行，每行包含一个正整数，依次为每一个询问的结果。

```cpp
#include <bits/stdc++.h>
using namespace std;
inline int read()
{
    char c=getchar();int x=0;
    for(;!isdigit(c);c=getchar());
    for(;isdigit(c);c=getchar())
        x=x*10+c-'0';
    return x;
}
//const int N=10005;
const int N=500005;
vector<int> G[N];
int n,m,FA[N][30],lg[N],DEP[N],s;

void dfs(int u,int fa)
{
    FA[u][0]=fa;
    DEP[u]=DEP[fa]+1;
    for(int i=1;i<lg[DEP[u]];i++)
        FA[u][i]=FA[FA[u][i-1]][i-1];
    for(int i=0;i<G[u].size();i++)
    {
        int v=G[u][i];
        if(fa!=v)
        {
            dfs(v,u);
        }
    }
}

int LCA(int x,int y)
{
    if(DEP[x]<DEP[y])swap(x,y);
    while(DEP[x]!=DEP[y])
        x=FA[x][ lg[DEP[x]-DEP[y]] -1 ] ;
    if(x==y)return x;
    for(int k=lg[DEP[x]]-1;k>=0;k--)
    if(FA[x][k]!=FA[y][k])
    {
        x=FA[x][k];
        y=FA[y][k];
    }
    return FA[x][0];
}

int main()
{
   cin>>n>>m>>s;
   
   for(int i=1;i<=n;i++)
        lg[i]=lg[i-1]+(i==(1<<lg[i-1]));
   
   for(int i=1;i<=n-1;i++)
    {
        int u=read();
        int v=read();
        G[u].push_back(v);
        G[v].push_back(u);
    }        
   dfs(s,0);
   

   for(int i=1;i<=m;i++)
   {
        int u=read();
        int v=read();
        printf("%d\n",LCA(u,v));
   }
   return 0;
}

```





## 割点

### 题目描述

给出一个 n*n* 个点，m*m* 条边的无向图，求图的割点。

### 输入格式

第一行输入两个正整数 n,m*n*,*m*。

下面 m*m* 行每行输入两个正整数 x,y*x*,*y* 表示 x*x* 到 y*y* 有一条边。

```cpp
#include <bits/stdc++.h>
using namespace std;

inline int read()
{
	char c = getchar(); int x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	return x;
}
const int N=20005;
int n,m,DFN[N],LOW[N],ts,cnt,cut[N];

bool in[N];
vector<int> G[N];

void Tarjan(int u,int fa)
{
    int s=0;
    DFN[u]=LOW[u]=++ts;
    for(int i=0;i<G[u].size();i++)
    {
        int v=G[u][i];
        if(DFN[v]==0)
        {
            Tarjan(v,u);
            LOW[u]=min(LOW[v],LOW[u]);
            if(fa==0)s++;
            else if(LOW[v]>=DFN[u])cut[u]=1;
        }
        LOW[u]=min(LOW[u],DFN[v]);
    }
    if(s>=2&&fa==0)cut[u]=1;
}
int main()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        int u=read();
        int v=read();
        G[u].push_back(v);
        G[v].push_back(u);
    }
    for(int i=1;i<=n;i++)if(DFN[i]==0)Tarjan (i,0);
    int ans=0;
    for(int i=1;i<=n;i++)if(cut[i])ans++;
    cout<<ans<<endl;
    for(int i=1;i<=n;i++)if(cut[i])cout<<i<<' ';
    return 0;
}


```



## 缩点

### 题目描述

给定一个 n*n* 个点 m*m* 条边有向图，每个点有一个权值，求一条路径，使路径经过的点权值之和最大。你只需要求出这个权值和。

允许多次经过一条边或者一个点，但是，重复经过的点，权值只计算一次#### 输入格式

第一行两个正整数 n,m*n*,*m*

第二行 n*n* 个整数，依次代表点权

第三至 m+2*m*+2 行，每行两个整数 u,v*u*,*v*，表示一条 u\rightarrow v*u*→*v* 的有向边。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N=10005,INF=0x3f3f3f3f;
int PW[N],DFN[N],LOW[N],n,m,ts,COL[N],cc,WT[N];
vector<int>G[N];
int g[N][N];
stack<int> S;
bool in[N];
inline int read()
{
	int x=0;char c=getchar();
	for(;!isdigit(c);c=getchar());
	for(; isdigit(c);c=getchar())
		x=x*10+c-'0';
	return x;
}

void Tarjan(int u)
{
	LOW[u]=DFN[u]=++ts;
	S.push(u);
	in[u]=1;
	for(int i=0;i<G[u].size();i++)
	{
		int v=G[u][i];
		if(!DFN[v])
		{L
			Tarjan(v);
			LOW[u]=min(LOW[u],LOW[v]);
		}
		else if(in[v])
		{
			LOwW[u]=min(LOW[v],LOW[u]);	
		}
	}
	if(DFN[u]==LOW[u])
	{
		cc++;
		while(1)
		{
			int x=S.top();
			S.pop();
			in[x]=0;
			
			COL[x]=cc;
			WT[cc]+=PW[x];
			if(x==u)break;
		}
	}
}

int f[N];
int dp(int u)
{
//	cout<<"DP:f"<<u<<"   "<<endl;
	if(f[u])return f[u];
	f[u]=WT[u];
	for(int i=1;i<=cc;i++)
	{
		if(g[u][i])
		{
			f[u]=max(f[u],dp(i)+WT[u]);	
		//	cout<<"INS"<<endl;
		}
	}
	return f[u];
}
			
			

int main()
{
	cin>>n>>m;
	for(int i=1;i<=n;i++)PW[i]=read();
	for(int i=1;i<=m;i++)
	{
		int u=read();
		int v=read();
		G[u].push_back(v);
	}
	for(int i=1;i<=n;i++)if(!DFN[i])Tarjan(i);
	
//	cout<<COL[1]<<" "<<COL[2]<<endl;
	
	for(int i=1;i<=n;i++)
	{	
		for(int j=0;j<G[i].size();j++)
		{
			int u=i,v=G[i][j];
			if(COL[u]!=COL[v])
			{
				g[COL[u]][COL[v]]=1;
			}
		}
	}
	
	int maxx=0;
	for(int i=1;i<=cc;i++)maxx=max(maxx,dp(i));
	cout<<maxx;
	
	return 0;
}
```





## 二分图最大匹配



#### 题目描述

给定一个二分图，其左部点的个数为 n*n*，右部点的个数为 m*m*，边数为 e*e*，求其最大匹配的边数。

左部点从 11 至 n*n* 编号，右部点从 11 至 m*m* 编号。

#### 输入格式

输入的第一行是三个整数，分别代表 n*n*，m*m* 和 e*e*。

接下来 e*e* 行，每行两个整数 u, v*u*,*v*，表示存在一条连接左部点 u*u* 和右部点 v*v* 的边。

#### 输出格式

输出一行一个整数，代表二分图最大匹配的边数。

```cpp
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <memory.h>

using namespace std;
const int maxn = 1005;
int edge[maxn][maxn];
int cx[maxn];
int cy[maxn];
int vis[maxn];
inline int read()
{
	int x = 0; char c = getchar();
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
	x = x * 10 + c - '0';
	return x;
}


int n, m, e;

int path(int u)
{
	int v;
	for (v = 1; v <= m; v++)
		if (edge[u][v] && !vis[v])
		{
			vis[v] = 1;
			if (cy[v] == -1 || path(cy[v]))
			{
				cx[u] = v;
				cy[v] = u;
				return 1;
			}
		}
	return 0;
}

int maxmatch()
{
	int res = 0;
	int u = 0;
	for (u = 1; u <= n; u++)
	{
		if (cx[u] == -1)
		{
			memset(vis, 0, sizeof(vis));
			res += path(u);
		}
	}
	return res;
}
int main()
{
	memset(cx, -1, sizeof(cx));
	memset(cy, -1, sizeof(cy));
	cin >> n >> m >> e;
	for (int i = 1; i <= e; i++)
	{
		int u = 0, v = 0;
		cin >> u >> v;
		//u = read();
		//v = read();
		if (v > m)continue;
		edge[u][v] = 1;
	}

	cout << maxmatch();

	return 0;
}
```



## 矩阵加速·数列



## 题目描述

已知一个数列 a*a*，它满足：
$$
a_x= \begin{cases} 1 & x \in\{1,2,3\}\\ a_{x-1}+a_{x-3} & x \geq 4 \end{cases}
$$


求 a*a* 数列的第 n*n* 项对 10^9+7109+7 取余的值。

## 输入格式

第一行一个整数 T*T*，表示询问个数。

以下 T*T* 行，每行一个正整数 n*n*。

## 输出格式

每行输出一个非负整数表示答案。

```cpp
#include <bits/stdc++.h>
#define ll long long 
using namespace std;

inline ll read()
{
	char c = getchar(); ll x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	return x;
}
const ll mod = 1e9 + 7, n = 3;
ll q;
struct Mat
{
	ll _[5][5];
	Mat()
	{
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				this->_[i][j] = 0;
	}
	Mat operator* (const Mat& A)const
	{
		Mat R;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				for (int k = 1; k <= n; k++)
					R._[i][j] = (R._[i][j] +( this->_[i][k] * A._[k][j])%mod)%mod;
		return R;
	}
};
Mat X,E;
Mat pww(ll k,Mat X)
{
	Mat A = E;
	while (k)
	{
		if (k & 1)
			A = A * X;
		X = X * X;
		k >>= 1;
	}
	return A;
}
int main()
{
	int T = read();
	for (int i = 1; i <= n; i++)E._[i][i] = 1;
	X._[1][1] = X._[1][3] = X._[2][1] = X._[3][2] = 1;
	while (T--)
	{
		q = read();
		Mat F=pww(q-1,X);
		ll ans = 0;
		for (int i = 1; i <= n; i++)
			ans = (ans+F._[3][i])%mod;
		printf("%lld\n", ans);
	}
	return 0;
}
```



**Dijkstra** 

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=100005,INF=0x3f3f3f3f;
int n,m,s,d[N];

inline int read()
{
    char c=getchar();int x=0;
    for(;!isdigit(c);c=getchar());
    for(;isdigit(c);c=getchar())
        x=x*10+c-'0';
    return x;
}

struct node
{
    int w,v;
    node(int a,int b)
    {
        w=a;
        v=b;
    }
};
vector<node>G[N];
priority_queue< pair<int,int> > Q;
bool vis[N];
void Dijk()
{
    memset(d,0x3f,sizeof(d));
    d[s]=0;
    Q.push( make_pair(0,s));

    while(!Q.empty())
    {
        int u=Q.top().second;
        Q.pop();
        if(vis[u])continue;
        vis[u]=1;
        for(int i=0;i<G[u].size();i++)
        {
            int v=G[u][i].v,w=G[u][i].w;
            if(d[v]>d[u]+w)
            {
                d[v]=d[u]+w;
                Q.push(make_pair(-d[v],v));
            }
        }
    }
}

int main()
{
    n=read();
    m=read();
    s=read();
    for(int i=1;i<=m;i++)
    {
        int u=read();
        int v=read();
        int w=read();
        G[u].push_back(node(w,v));
    }
    Dijk();
    for(int i=1;i<=n;i++)
        printf("%d ",d[i]);

    return 0;
}
```



## 负环



#### 题目描述

给定一个 n*n* 个点的有向图，请求出图中是否存在**从顶点 11 出发能到达**的负环。

负环的定义是：一条边权之和为负数的回路。

#### 输入格式

**本题单测试点有多组测试数据**。

输入的第一行是一个整数 T*T*，表示测试数据的组数。对于每组数据的格式如下：

第一行有两个整数，分别表示图的点数 n*n* 和接下来给出边信息的条数 m*m*。

接下来 m*m* 行，每行三个整数 u, v, w*u*,*v*,*w*。

-   若 w \geq 0*w*≥0，则表示存在一条从 u*u* 至 v*v* 边权为 w*w* 的边，还存在一条从 v*v* 至 u*u* 边权为 w*w* 的边。
-   若 w < 0*w*<0，则只表示存在一条从 u*u* 至 v*v* 边权为 w*w* 的边。

#### 输出格式

对于每组数据，输出一行一个字符串，若所求负环存在，则输出 `YES`，否则输出 `NO`。

```cpp
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <list>
#include <memory.h>
using namespace std;
int n, m;
const int maxn = 20005;
struct edge
{
	int to, w;
	edge()
	{
		to = 0;
		w = 0;
	}
	edge(int a, int b)
	{
		to = a;
		w = b;
	}
};
vector< vector<edge> > G;
int d[maxn];
const int INF = 1 << 30;
int cnt[maxn];
bool flag = 1;
bool v[maxn];
inline int read()
{
	bool minus = 0;
	int x = 0; char c = getchar();
	for (; !isdigit(c); c = getchar())
		if (c == '-')minus = 1;
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	if (minus)return -x;
	return x;
}

inline void intial()
{
	G.clear();
	memset(v, 0, sizeof(v));
	for (int i = 0; i < maxn; i++)
		d[i] = INF;
	memset(cnt, 0, sizeof(cnt));
}

struct node
{
	int x;
	node(int a)
	{
		x = a;
	}
	bool operator <(const node& i)const
	{
		return this->x > i.x;
	}
};

void SPFA(int start)
{
	priority_queue<node> Q;
	//list<int>Q;
	Q.push(node(start));
	v[start] = 1;
	d[start] = 0;
	cnt[start] = 1;
	while (!Q.empty())
	{
		int x = Q.top().x;
		Q.pop();
		v[x] = 0;
		for (int i = 0; i < G[x].size(); i++)
		{
			int t = G[x][i].to, w = G[x][i].w;
			if (d[x] + w < d[t])
			{
				d[t] = d[x] + w;
				cnt[t] = cnt[x] + 1;

				if (!v[t])
				{
					if (cnt[t] > n)
					{
						flag = 0;
						return;
					}
					v[t] = 1;
					Q.push(node(t));
				}
			}
		}
	}
}

int main()
{
//	freopen("C:\\Users\\Administrator\\Downloads\\testdata (16).in", "r", stdin);
	int oo;
	oo = read();
	for (int pp = 1; pp <= oo; pp++)
	{
		flag = 1;
		intial();
		n = read();
		m = read();
		vector<edge>samp;
		G.assign(n + 10, samp);
		for (int i = 1; i <= m; i++)
		{
			int a, b, w;
			a = read();
			b = read();
			w = read();
			if (w < 0)
			{
				G[a].push_back(edge(b, w));
			}
			else
			{
				G[a].push_back(edge(b, w));
				G[b].push_back(edge(a, w));
			}
		}

		SPFA(1);

		if (flag == 0)
			cout << "YE5" << endl;
		if (flag)
			cout << "N0" << endl;
	}
	return 0;
}
```



## 树状数组

#### 题目描述

如题，已知一个数列，你需要进行下面两种操作：

1.  将某区间每一个数数加上 x*x*；
2.  求出某一个数的值。

#### 输入格式

第一行包含两个整数 N*N*、M*M*，分别表示该数列数字的个数和操作的总个数。

第二行包含 N*N* 个用空格分隔的整数，其中第 i*i* 个数字表示数列第 i*i* 项的初始值。

接下来 M*M* 行每行包含 22 或 44个整数，表示一个操作，具体如下：

操作 11： 格式：`1 x y k` 含义：将区间 [x,y][*x*,*y*] 内每个数加上 *k*；

操作 22： 格式：`2 x` 含义：输出第 *x* 个数的值。

#### 输出格式

输出包含若干行整数，即为所有操作 22 的结果。

```cpp
// Segtree.cpp: 定义控制台应用程序的入口点。
//


#include <bits/stdc++.h>
#define ll long long 
#define mid ((L+R)>>1)
#define ls (o<<1)
#define rs (o<<1|1)
#define len (R-L+1)
using namespace std;

inline ll read()
{
	char c = getchar(); ll x = 0;
	bool minus = 0;
	for (; !isdigit(c); c = getchar())
		if (c == '-')minus = 1;
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	if (minus)return -x;
	return x;
}
const ll N = 1000001;
ll n, m, l, r, dlt, nowsum;
ll a[N], sum[N << 1], tag[N << 1];

inline void push_up(ll o)
{
	sum[o] = sum[ls] + sum[rs];
}

void construct(ll o, ll L, ll R)
{
	tag[o] = 0;
	if (L == R)
	{
		sum[o] = a[L];
		return;
	}
	construct(ls, L, mid);
	construct(rs, mid + 1, R);
	push_up(o);
}

inline void ff(ll o, ll L, ll R, ll d)
{
	tag[o] += d;
	sum[o] += d * len;
}

inline void push_down(ll o, ll L, ll R)
{
	ff(ls, L, mid, tag[o]);
	ff(rs, mid + 1, R, tag[o]);
	tag[o] = 0;
}

void update(ll o, ll L, ll R)
{
	if (l <= L && R <= r)
	{
		tag[o] += dlt;
		sum[o] += dlt * len;
		return;
	}
	push_down(o, L, R);
	if (l <= mid)update(ls, L, mid);
	if (r > mid)update(rs, mid + 1, R);
	push_up(o);
}

ll query(ll o, ll L, ll R)
{
	if (l <= L && R <= r)
	{
		return  sum[o];
	}
	ll res = 0;
	push_down(o, L, R);
	if (l <= mid)res += query(ls, L, mid);
	if (r > mid)if (r > mid)res += query(rs, mid + 1, R);
	push_up(o);
	return res;
}


int main()
{
	cin >> n >> m;
	for (ll i = 1; i <= n; i++)
		a[i] = read();
	construct(1, 1, n);
	while (m--)
	{
		ll q = read();
		if (q == 1)
		{
			l = read();
			r = read();
			dlt = read();
			update(1, 1, n);

		}
		if (q == 2)
		{
			l = read();
			r = l;
			printf("%lld\n", query(1, 1, n));
		}
	}

	return 0;
}


```





## Dicnic 网络最大流

#### 题目描述

如题，给出一个网络图，以及其源点和汇点，求出其网络最大流。

#### 输入格式

第一行包含四个正整数 n,m,s,t*n*,*m*,*s*,*t*，分别表示点的个数、有向边的个数、源点序号、汇点序号。

接下来M行每行包含三个正整数 u_i,v_i,w_i*u**i*,*v**i*,*w**i*，表示第 i*i* 条有向边从 u_i*u**i* 出发，到达 v_i*v**i*，边权为 w_i*w**i*（即该边最大流量为 w_i*w**i*）。

#### 输出格式

一行，包含一个正整数，即为该网络的最大流。

```cpp
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <memory.h>
using namespace std;
const int maxn = 10005;
const int maxm = 1000005 * 2;//边数max
const int INF = 1 << 30;
int  ind = 0;
int r[maxm];//残余流量
int vec[maxm];//编号x的边指向的点
int dep[maxn];//点的层次编号数组
list<int>G[maxn];//记录每个点的出边
inline int read()
{
	char c = getchar(); int x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	return x;
}

int bfs(int s, int t)
{
	queue<int>Q;
	while (!Q.empty())Q.pop();
	memset(dep, 0, sizeof(dep));
	dep[s] = 1;
	Q.push(s);

	while (!Q.empty())
	{
	//	cout << "*****bfs1****" << endl;
		int x = Q.front();
		Q.pop();

		for (list<int>::iterator it = G[x].begin(); it != G[x].end(); it++)
		{
			int i = *it;
			if ((r[i] > 0) && (dep[vec[i]] == 0))
			{
			//	cout << "*****bfs2****x=" << x << endl;
				dep[vec[i]] = dep[x] + 1;
				Q.push(vec[i]);
			}
		}


	}
	if (dep[t] > 0)return 1;
	if (dep[t] == 0)return 0;

}

int dfs(int s, int mxfl, int t)
{
	if (s == t)return mxfl;
	for (list<int>::iterator it = G[s].begin(); it != G[s].end(); it++)
	{
		int i = *it;
		//cout << "&****dfs 1************" << endl;
		if ((dep[vec[i]] == dep[s] + 1) && (r[i] > 0))
		{
			//cout << "&****dfs2************" << endl;
			int di = dfs(vec[i], min(r[i], mxfl), t);
			//cout << "&***dfs3************" << endl;
			//cout << "di=" << di << endl;
			if (di > 0)
			{
				r[i] -= di;
				r[i ^ 1] += di;
				return di;
			}
		}
	}
	return 0;
}

inline void add(int u, int v, int w)
{
	r[ind] += w;

	G[u].push_back(ind);
	vec[ind] = v;
	ind++;
}

int Dinic(int s, int t)
{
	int maxflow = 0;
	while (bfs(s, t))
	{
	//	cout << "&****dinic 1************" << endl;
		while (1)
		{
		//	cout << "&****dinic 1************" << endl;
			int d = dfs(s, INF, t);
			if (d == 0)break;
			maxflow += d;

		}
	}
	return maxflow;
}

int main()
{

	int n, m, s, t;
	cin >> n >> m >> s >> t;
	for (int i = 1; i <= m; i++)
	{
		int u, v, w;
		u = read();
		v = read();
		w = read();
		add(u, v, w);
		add(v, u, 0);

	}


	cout << Dinic(s, t);

	return 0;
}


```





## **线段树**：动态区间

### 题目描述

如题，已知一个数列，你需要进行下面三种操作：

-   将某区间每一个数乘上 x*x*
-   将某区间每一个数加上 x*x*
-   求出某区间每一个数的和

#### 输入格式

第一行包含三个整数 n,m,p*n*,*m*,*p*，分别表示该数列数字的个数、操作的总个数和模数。

第二行包含 n*n* 个用空格分隔的整数，其中第 i*i* 个数字表示数列第 i*i* 项的初始值。

接下来 m*m* 行每行包含若干个整数，表示一个操作，具体如下：

操作 11： 格式：`1 x y k` 含义：将区间 [x,y][*x*,*y*] 内每个数乘上 k*k*

操作 22： 格式：`2 x y k` 含义：将区间 [x,y][*x*,*y*] 内每个数加上 k*k*

操作 33： 格式：`3 x y` 含义：输出区间 [x,y][*x*,*y*] 内每个数的和对 p*p* 取模所得的结果

```cpp
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <memory.h>

#define ll long long 
using namespace std;

const int maxn = 100005;
const int maxm = 1000005;
ll a[maxn];
ll sum[maxm];
ll addv[maxm];
ll mulv[maxm];
int p;
inline ll read()
{
	char c = getchar(); ll x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + (c - '0');
	return x;
}


void  cons(int o, int L, int R)
{
	addv[o] = 0;
	mulv[o] = 1;
	if (L == R)
		sum[o] = a[L];
	else
	{
		int mid = (L + R) / 2;
		cons(o * 2, L, mid);
		cons(o * 2 + 1, mid + 1, R);
		sum[o] = sum[o * 2] + sum[o * 2 + 1];
	}
	sum[o] %= p;
	return;
}


inline void maintain(int o, int L, int R)
{
	int mid = (L + R) / 2;
	sum[o * 2] = (sum[o * 2] * mulv[o] + addv[o] * (mid - L + 1)) % p;
	sum[o * 2 + 1] = (sum[o * 2 + 1] * mulv[o] + addv[o] * (R - mid)) % p;

	mulv[o * 2] = (mulv[o] * mulv[o * 2]) % p;
	mulv[o * 2 + 1] = (mulv[o] * mulv[o * 2 + 1]) % p;
	addv[o * 2] = (addv[o * 2] * mulv[o] + addv[o]) % p;
	addv[o * 2 + 1] = (addv[o * 2 + 1] * mulv[o] + addv[o]) % p;

	addv[o] = 0;
	mulv[o] = 1;
}


ll ql, qr;
void u_add(int o, int L, int R, int d)
{
	if (R<ql || L>qr)return;
	if (ql <= L && R <= qr)
	{
		addv[o] = (addv[o] + d) % p;
		sum[o] = (sum[o] + d * (R - L + 1)) % p;
		return;
	}

	maintain(o, L, R);
	int mid = (L + R) / 2;
	u_add(2 * o, L, mid, d);
	u_add(2 * o + 1, mid + 1, R, d);
	sum[o] = (sum[o * 2] + sum[o * 2 + 1]) % p;
	return;



}

void u_mul(int o, int L, int R, int m)
{
	if (R<ql || L>qr)return;
	if (ql <= L && R <= qr)
	{
		sum[o] = (sum[o] * m) % p;
		addv[o] = (addv[o] * m) % p;
		mulv[o] = (mulv[o] * m) % p;
		return;
	}
	maintain(o, L, R);
	int mid = (L + R) / 2;
	u_mul(2 * o, L, mid, m);
	u_mul(2 * o + 1, mid + 1, R, m);
	sum[o] = (sum[o * 2] + sum[o * 2 + 1]) % p;
	return;



}


ll query(int o, int L, int R)//intial d=0,m=1;
{
	if (R<ql || L>qr)return 0;
	if (ql <= L && R <= qr)
		return sum[o];

	ll s1 = 0, s2 = 0;
	maintain(o, L, R);
	int mid = (L + R) / 2;
	s1 = query(2 * o, L, mid);
	s2 = query(2 * o + 1, mid + 1, R);
	return (s1 + s2) % p;
}

int main()
{
	memset(mulv, 1, sizeof(mulv));
	int n, m;
	cin >> n >> m >> p;
	for (int i = 1; i <= n; i++)
		a[i] = read();
	cons(1, 1, n);
	for (int i = 1; i <= m; i++)
	{
		ll g = 0;
		g = read();
		ql = read();
		qr = read();
		if (g == 1)
		{
			int k = read();
			u_mul(1, 1, n, k);
			continue;
		}
		if (g == 2)
		{
			int k = read();
			u_add(1, 1, n, k);
			continue;
		}
		if (g == 3)
		{
			ll s = query(1, 1, n);
			printf("%d\n", s);
			continue;
		}
	}
	return 0;
}


```





## ST表：静态区间

#### 题目描述

给定一个长度为 N* 的数列，和 *M* 次询问，求出每一次询问的区间内数字的最大值。

#### 输入格式

第一行包含两个整数 , M*,*M* ，分别表示数列的长度和询问的个数。

第二行包含 N* 个整数（记为 a_i），依次表示数列的第 *i* 项。

接下来 M*行，每行包含两个整数 l_i, r_i*，表示查询的区间为 [ l_i, r_i][*l**i*,*r**i*]

#### 输出格式

输出包含 M*行，每行一个整数，依次表示每一次询问的结果。

```cpp
// P3865_4.cpp: 定义控制台应用程序的入口点。
//


#include <bits/stdc++.h>
#define ll long long 
using namespace std;
const int N = 1e5 + 5, M = 1e6 + 5;
int n, m;

inline int read()
{
	char c = getchar(); int x = 0;
	for (; !isdigit(c); c = getchar());
	for (; isdigit(c); c = getchar())
		x = x * 10 + c - '0';
	return x;
}
int maxx[N][50];
ll lg[50];

inline void init()
{
	lg[0] = 1;
	for (int i = 1; i <= 21; i++)lg[i] = (lg[i - 1] << 1);
	int i=1;
	for (int j = 1; j<=21; j++)
	{
		for ( i = 1; i + lg[j]-1<= n; i++)
		{
			maxx[i][j] = max(maxx[i][j - 1], maxx[i + lg[j - 1]][j - 1]);
		}
	}

}
int main()
{
	cin >> n >> m;
	for (int i = 1; i <= n; i++)maxx[i][0] = read();
	init();
	for (int i = 1; i <= m; i++)
	{
		int l = read();
		int r = read();
		int k = log2(r - l + 1);
		int ans = max(maxx[l][k], maxx[r - lg[k] + 1][k]);
		printf("%d\n", ans);
	}


	return 0;
}


```







