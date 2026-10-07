##第27关：均方差计算
##【题目描述】计算N个数的均方差。若将 N 个数的平均值记为 Avg，则该N个数的均方差计算公式为： , 其中A1，A2,…,An为该数列中的N个数。
##【输入描述】一行，若干小数以空格分隔。
##【输出描述】输出均方差，保留三位小数。
##【输入样例】0 0 2 2
##【输出样例】1.000

value_ = 0
li = input().split()
Avg = sum(map(float,li)) / len(li)
# print(Avg)

for i in li:
    zhi = (float(i) - Avg)**2
    value_ += zhi

total = (value_ / len(li))**0.5
print("{:.3f}".format(total))
