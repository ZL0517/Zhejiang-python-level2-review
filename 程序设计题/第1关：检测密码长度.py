##第1关：检测密码长度
##程序功能：当前各种系统一般需要用户注册，并设置密码。
##本题目规定有效的密码必须符合长度大于等于8；
##编写一个程序确认密码是否有效；如果有效输出True，否则输出False。
##【输入描述】一行字符串，表示密码。
##【输出描述】是否有效，如果是输出True，否则输出False。
##【输入样例】abcW2121 
##【输出样例】True

a=input( )
if len(a)>=8:
    print(True)
else:
    print(False)


mm=input()
if len(mm)>=8:
    z=True
else:
    z=False
print(z)


