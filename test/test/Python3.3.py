# filename='Test_file/learning_python.txt'
# with open(filename) as file_obj:
#     content=file_obj.read()
# print(content.rstrip())
# print("_______________________________")
# with open(filename) as file_obj:
#     for line in file_obj:
#         print(line.rstrip())
# print("_______________________________")
# with open(filename) as file_obj:
#     lines=file_obj.readlines()
# for line in lines:
#     print(line.rstrip())

# filename='Test_file/guest.txt'
# with open(filename,mode='w') as file_obj:
#     name=input("请输入姓名:")
#     file_obj.write(name)

# filename='Test_file/guest_book.txt'
# while True:
#     name=input("请输入姓名（输入quit退出输入）:")
#     if name=='quit':break
#     name=f'Hello {name}!'
#     print(name)
#     with open(filename,mode='a') as file_obj:
#         file_obj.write(name+'\n')

# a=input('请输入第一个数：')
# b=input('请输入第二个数：')
# try:
#     num1=int(a)
#     num2=int(b)
# except ValueError:
#     print('输入不合法！！！！！')
# else:
#     print(num1+num2)

# while True:
#     a=input("请输入第一个数：")
#     b=input("请输入第二个数：")
#     if a=='quit'or b=='quit':break
#     try:
#         num1=int(a)
#         num2=int(b)
#     except ValueError:
#         print('输入不合法！！！！！')
#     else:
#         print(num1+num2)

# import json
# filename='Test_file/favoriteNumber.txt'
# number=input("请输入一个你喜欢的数字：")
# with open(filename,mode='w') as file_obj:
#     json.dump(number,file_obj)
#
# try:
#     with open(filename,'r') as file_obj:
#         context=json.load(file_obj)
# except FileNotFoundError:
#     print("不存在该文件!!!")
# else:
#     print("I know your favorite number! It's "+context+'.')

# import json
# filename='Test_file/favoriteNumber.txt'
# try:
#     with open(filename,'r') as file_obj:
#         context=json.load(file_obj)
# except FileNotFoundError:
#     number=input("请输入一个你喜欢的数字：")
#     with open(filename,mode='w') as file_obj:
#         json.dump(number,file_obj)
# else:
#     print("I know your favorite number! It's "+context+'.')


# filename='D:\Python\源代码文件\源代码文件\chapter_10\pi_million_digits.txt'
# with open(filename,mode='r') as file_obj:
#     context=file_obj.readlines()
# pi=''
# for line in context:
#     pi+=line.strip()
# new_pi=pi[:1000002]
# days={
#     1:31,
#     2:28,
#     3:31,
#     4:30,
#     5:31,
#     6:30,
#     7:31,
#     8:31,
#     9:30,
#     10:31,
#     11:30,
#     12:31
# }
# flag=False
# for month in range(1,13):
#     for day in range(1,days[month]+1):
#         number='{0:0>2d}{1:0>2d}'.format(month,day)
#         # print(number)
#         if number in new_pi:
#             print(number+'已出现在圆周率中')
#             flag=True
#             break
#     if flag==True:break
# if flag==False:print("没有出现在圆周率中")

# days={
#     1:31,
#     2:28,
#     3:31,
#     4:30,
#     5:31,
#     6:30,
#     7:31,
#     8:31,
#     9:30,
#     10:31,
#     11:30,
#     12:31
# }
# def check(year):
#     if year%400==0:return True
#     elif year%4==0 and year%100!=0:return True
#     else:return False
#
# if __name__=='__main__':
#     filename='D:\Python\源代码文件\源代码文件\chapter_10\pi_million_digits.txt'
#     with open(filename,mode='r') as file_obj:
#         context=file_obj.readlines()
#     pi=''
#     for line in context:
#         pi+=line.strip()
#     new_pi=pi[:1000002]
#
#     for year in range(2001,2021):
#         if check(year)==True:days[2]=29
#         else:days[2]=28
#         for month in range(1, 13):
#             for day in range(1,days[month]+1):
#                 number = '{0}{1:0>2d}{2:0>2d}'.format(year,month, day)
#                 if number in new_pi:
#                     print(number+'在圆周率小数点前一百万位中')

# def get(name):
#     bytes_name=bytes(name,encoding="UTF-8")
#     decimal_name=int.from_bytes(bytes_name,'big')
#     new_decimal_name=str(decimal_name)
#     return new_decimal_name
# if __name__=='__main__':
#     name1=input("请输入英文姓名：")
#     name2=input("请输入中文姓名：")
#     filename='D:\Python\源代码文件\源代码文件\chapter_10\pi_million_digits.txt'
#     with open(filename,mode='r') as file_obj:
#         context=file_obj.readlines()
#     pi=''
#     for line in context:
#         pi+=line.strip()
#     new_pi=pi[:1000002]
#     decimal_name={
#         name1:get(name1),
#         name2:get(name2)
#     }
#     for key in decimal_name.keys():
#         if decimal_name[key] in new_pi:
#             print(key+"转化为十进制字符串出现在圆周率前一百位内！")
#         else:print(key+"转化为十进制字符串没有出现在圆周率前一百位内！")

# with open("D:\Python\Alice in wonderland.txt",mode='r',encoding='UTF-8') as file_obj:
#     content=file_obj.read()
#
# symbol=[",",".",":","[","]","#","*","?","!","(",")",'“',"\n","/",'"','”']
# content=content.lower()
# for sy in symbol:
#     content=content.replace(sy," ")
# list_content=content.split()
# count={}
# for mes in list_content:
#     if len(mes)<5:continue
#     if mes not in count:
#         count[mes]=1
#     else:count[mes]+=1
# sort_count=dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
# cnt=0
# for key in sort_count:
#     if cnt==7:break
#     print(key+" "+str(count[key]))
#     cnt+=1

# import json
# username=input("请输入用户名：")
# password=input("请输入密码：")
# dic={
#     "username":username,
#     "password":password
# }
# with open("Test_file/account.txt",mode='w') as file_obj:
#     json.dump(dic,file_obj)

# import json
# with open("Test_file/account.txt",mode='r') as file_obj:
#     data=json.load(file_obj)
# username=input("请输入用户名：")
# password=input("请输入密码：")
# if username==data["username"] and password==data["password"]:
#     print("登录成功！")
# else:print("用户名或密码错误！")

import json
with open("Test_file/account.txt",mode='r') as file_obj:
    data=json.load(file_obj)
username=input("请输入用户名：")
password=input("请输入密码：")
if username==data["username"] and password==data["password"]:
    while True:
        new_password=input("请输入新密码：")
        if new_password==password:print("新密码与原密码相同！！")
        else:
            data["password"]=new_password
            with open('Test_file/account.txt',mode='w') as file_obj:
                json.dump(data,file_obj)
            break
else:print("用户名或密码错误！")
print(data)




