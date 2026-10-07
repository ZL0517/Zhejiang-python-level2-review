##第29关：学生判断题的最高分
##程序功能：n个学生参加一场测试，测试只有m道判断题，每题分值为2分。根据标准答案和n个同学的解答，统计并输出最高得分。
##【输入描述】第1行包含两个整数，分别为n和m的值。第2行是标准答案，接下来n行依次为每个学生的解答。标准答案和每个学生的解答均为长度是m的字符串，其中仅含字符T和F。
##【输出描述】一个整数，为所有学生中的最高分。
##【输入样例】3 6
##FFTFTT
##FTTFFF
##FFTFFT
##TFTFTF
##【输出样例】10

n,m = list(map(int,input().split()))
keys = input()

t = []
for i in range(n):
    t.append(input())

t2 = []
for x in t:
    score = 0
    for i in range(m):
        if x[i] == keys[i]:
            score = score + 2

    t2.append(score)

print(max(t2))
