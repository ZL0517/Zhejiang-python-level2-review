##第21关：会员购物金额
##程序功能：某店铺有非会员、普通会员、银会员、金会员。
##普通会员购物95折，银会员购物90折，金会员85折。
##店铺销售商品只有3种：商品一、商品二、商品三，价格分别是100元、200元、300元。
##输入会员级别、商品名、商品数量，输出购物金额。
##【输入描述】2个字符串、1个正整数（用空格隔开），分别表示会员级别、商品名、商品数量。
##【输出描述】1个整数，表示购物金额。
##【输入样例】金会员 商品一 100
##【输出样例】8500

level, goods, num = input().split()
num = int(num)
price = {"商品一": 100, "商品二": 200, "商品三": 300}[goods]
rate = {"非会员": 1.0, "普通会员": 0.95, "银会员": 0.90, "金会员": 0.85}[level]
print(int(price * num * rate))



hy,sp,count = input().split()
count = int(count)
if hy == "非会员":
    if sp == "商品一":
       fee = 100 * count
    elif sp == "商品二":
         fee = 200 * count
    elif sp == "商品三":
         fee = 300 * count

if hy == "普通会员":
    if sp == "商品一":
       fee = 100 * count * 0.95
    elif sp == "商品二":
         fee = 200 * count * 0.95
    elif sp == "商品三":
         fee = 300 * count * 0.95
if hy == "银会员":
    if sp == "商品一":
       fee = 100 * count * 0.9
    elif sp == "商品二":
         fee = 200 * count * 0.9
    elif sp == "商品三":
         fee = 300 * count * 0.9

if hy == "金会员":
    if sp == "商品一":
       fee = 100 * count * 0.85
    elif sp == "商品二":
         fee = 200 * count * 0.85
    elif sp == "商品三":
         fee = 300 * count * 0.85
print(int(fee))
