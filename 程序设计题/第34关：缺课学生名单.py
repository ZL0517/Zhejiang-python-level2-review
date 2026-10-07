##第34关：缺课学生名单
##程序功能：输入一个小组的学生名单，再输入一个到课学生名单，请编写程序，输出缺课学生名单。忽略英文名中的大小写。提示：①列表ls中移除x元素的可使用ls.remove(x);②返回字符串str的副本，并全部字符转为小写可使用str.lower()。
##【输入描述】二行，一行为小组学生名单，另一行为到课学生名单，名字间用空格分隔。
##【输出描述】缺课学生名单。
##【输入样例】张三 李四 王五 赵六 Lily Jack
##王五 赵六 jack 张三
##【输出样例】李四 Lily

names = input().split()
dk = input().split()


dk = [x.lower() for x in dk]
for x in names:
    if x.lower() not in dk:
        print(x, end = " ")
