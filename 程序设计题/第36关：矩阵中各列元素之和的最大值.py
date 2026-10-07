##第36关：矩阵中各列元素之和的最大值
##程序功能：给定m行n列的整型数据构成的矩阵（m≤20，n≤10），计算该矩阵中各列元素之和，并输出其中的最大值。
##【输入格式】第一行包含2个整数，为m和n的值；接下来有m行，每行包含n个整数。
##【输出格式】一个整数，表示该矩阵中各列元素之和的最大值。
##【输入样例】3 4
##1 2 3 4
##5 6 7 8
##9 10 11 12
##【输出样例】24

m,n = map(int,input().split())

t = []
for i in range(m):
    t.append(list(map(int,input().split())))

s = []
for i in range(n):
    sum_ = 0
    for j in range(m):
        sum_ = sum_ + t[j][i]

    s.append(sum_)

print(max(s))
