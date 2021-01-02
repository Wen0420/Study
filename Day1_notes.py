#给定一个数字，取二进制
n = 100
bin(100)[2:]

#三进制 base 3
result = ""
while n >= 0:
    m = n % 3
    result += str(m)
    n = n // 3
#或者
result = ""
while n >= 0:
    n,a = divmod(n,3)#第一个是除数，第二个是余数
    result += str(a)

#假设有一个题n = 1000000怎么知道1后面有几个零
n = 1000000
count = 0
while n >= 0:
    n,a = divmod(n,10)
    if a == 0:
        count +=1
    else:
        break
#或者
n = 1000000
str_n = str(n)
str_n.strip("0")#把后面的0 去掉他们的差相减
len(str(n))-len(str(n).strip("0"))

#n = "0000100002003001000000" 问中间有多少个0
n = "0000100002003001000000"
str(n).strip("0").count("0")




