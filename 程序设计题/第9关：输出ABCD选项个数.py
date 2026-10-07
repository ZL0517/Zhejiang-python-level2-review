##第9关：输出ABCD选项个数
##程序功能：单项选择题供选答案有四项：A、B、C、D。输入10道单项选择题的答案，分别计算答案中四个选项的个数。
##【输入描述】一个字符串，10道单项选择题的答案，以空格隔开。
##【输出描述】四行输出，分别输出A选项B选项C选项D选项的个数。
##【输入样例】A B C D A D D C B B
##【输出样例】A选项2个 B选项3个 C选项2个 D选项3个

key = input()

print("A选项{}个".format(key.count("A")))
print("B选项{}个".format(key.count("B")))
print("C选项{}个".format(key.count("C")))
print("D选项{}个".format(key.count("D")))


key = input()
print("A选项"+str(key.count("A"))+"个")
print("B选项"+str(key.count("B"))+"个")
print("C选项"+str(key.count("C"))+"个")
print("D选项"+str(key.count("D"))+"个")
