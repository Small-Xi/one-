print("please input your name！");
a=input("请输入你的名字：");
print("Hello!  "+ a + "！");

import random
b=int(input("请输入你的参数："))
while b>0:
    print(random.randint(0,100))
    b-=1

# 输出字符串的长度、字符串的前两个字符，字符串的后两个字符、不包括最后一个字符的字符串；
c=str(input("请输入字符串："))
print("字符串的长度是："+ str(len(c)))
print("字符串的前两个字符："+c[0:2])
print("字符串的后两个字符："+c[(len(c)-2):len(c)])
print("不包括最后一个字符的字符串："+c[(len(c)-3):(len(c)-1)])