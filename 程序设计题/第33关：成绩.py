##第33关：成绩
##程序功能：给定m位学生n门课程的成绩（m≤20，n≤10），以及达标线。统计并输出各门课程的平均分在达标线以上的学生人数。
##【输入格式】第一行包含2个整数，为m和n的值；接下来有m行，每行包含n个正整数，为1位学生的n门课程的成绩。最后一行包含一个整数，为达标线。
##【输出格式】一个整数，表示平均分在达标线以上的学生人数。
##【输入样例】3 4
##72 85 76 91
##67 62 68 99
##78 71 89 82
##75
##【输出样例】2

m,n = map(int, input().split())

avglst = []
for i in range(m):
    scores = list(map(int,input().split()))
    avglst.append(sum(scores)/len(scores))

dbx = int(input())

count = 0
for x in avglst:
    if x >= dbx:
        count +=1

print(count)
