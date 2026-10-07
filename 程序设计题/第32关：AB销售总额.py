##第32关：AB销售总额
##程序功能：某公司销售部分AB两组，对销售部员工的销售额按组进行统计。
##【输入描述】第一行输入一个整数N，然后再输入N行数据，每行两个字符串和一个整数，分别对应员工姓名、级别，销售额。
##【输出描述】分行输出AB两组的销售总额，并在最后一行销售额总计。
##【输入样例】4
##张三 A 1500
##李四 B 2000
##赵六 A 2500
##王七 B 1200
##【输出样例】A 4000
##B 3200
##ALL 7200

n = int(input())

sumA = 0
sumB = 0

for i in range(n):
    name,group,sale = input().split()
    sale = int(sale)

    if group == 'A':
        sumA += sale
    if group == 'B':
        sumB += sale
print('A', sumA)
print('B', sumB)
print('ALL', sumA + sumB)
