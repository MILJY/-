# def display_message():
#     print("本章我学到了函数的使用")
# if __name__=='__main__':
#     display_message()

# def make_shirt(size,words):
#     print("衣服的尺码为："+size+"，标语为："+words)
# if __name__=='__main__':
#     make_shirt('XL','中国')
#     make_shirt(words='中国',size='XL')

# def make_shirt(size,words='I love Python'):
#     print("衣服的尺码为："+size+"，标语为："+words)
# if __name__=='__main__':
#     make_shirt('大号')
#     make_shirt('中号')
#     make_shirt('小号','I love C++')

# def make_album(singer,album):
#     dic={'singer_name':singer,'album_name':album}
#     return dic
# if __name__=='__main__':
#     JJ=make_album('林俊杰','爱笑的眼睛')
#     LXY=make_album('蓝心雨','突然一场雨')
#     SXJ=make_album('苏星婕','眼睛下暴雨')
#     print(JJ)
#     print(LXY)
#     print(SXJ)

# def make_album(singer,album):
#     dic={'singer_name':singer,'album_name':album}
#     return dic
#
# if __name__=='__main__':
#     while True:
#         name=input("请输入歌手名字")
#         album=input('请输入歌手专辑名')
#         dic=make_album(name,album)
#         print(dic)
#         op=input('是否继续输入（Y：是，N：否）')
#         if op=='N':break

# def show_messages(messages,sent_messages):
#     while messages:
#         book=messages.pop()
#         print(f"书名为:{book.title()}")
#         sent_messages.append(book.title())
#
# def send_messages(messages,sent_messages):
#     print(messages)
#     print(sent_messages)
# if __name__=='__main__':
#     messages=['c++','java','python']
#     sent_messages=[]
#     show_messages(messages[:],sent_messages)
#     send_messages(messages,sent_messages)

# def make_car(manufacturer,type,**info):
#     dic={}
#     dic['manufacturer']=manufacturer
#     dic['type']=type
#     for key,value in info.items():
#         dic[key]=value
#     return dic
# if __name__=='__main__':
#     car = make_car('subaru', 'outback', color='blue', tow_package=True)
#    print(car)

# def solve(x):
#     sum=0
#     while x:
#         sum+=x%10
#         x/=10
#     return sum
# list=[123,125,569,125,1236,9563,14]
# list.sort(key=lambda x:solve(x))
# print(list)

# list1=[123,125,569,125,1236,9563,14]
# new_list=list(map(lambda x:x**2+1,list1))
# print(new_list)

# companies = {
# 'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
# 'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
# 'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
#
# company=[key for key in companies.keys() if any(value<9 for value in companies[key].values())]
# print(company)

# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name+" "+self.cuisine_type)
#
#     def open_restaurant(self):
#         print("餐馆正在营业中！！")
# if __name__=='__main__':
#      restaurant=Restaurant('CCSU__MI','湘菜')
#      print(restaurant.restaurant_name)
#      print(restaurant.cuisine_type)
#      restaurant.describe_restaurant()
#      restaurant.open_restaurant()

# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name+" "+self.cuisine_type)
#
#     def open_restaurant(self):
#         print("餐馆正在营业中！！")
#
#     def set_number_served(self,number_served):
#         self.number_served=number_served
#
#     def get_number_served(self):
#         return self.number_served
#
#     def increment_number_served(self,number):
#         self.number_served+=number
#
# if __name__=='__main__':
#      restaurant=Restaurant('CCSU__MI','湘菜')
#      restaurant.describe_restaurant()
#      restaurant.open_restaurant()
#      print(f"招待人数：{restaurant.get_number_served()}")
#      restaurant.set_number_served(3)
#      print(f"招待人数：{restaurant.get_number_served()}")
#      restaurant.increment_number_served(5)
#      print(f"招待人数：{restaurant.get_number_served()}")


# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type,number_served):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=number_served
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} {self.cuisine_type} {self.number_served}")
#
#     def get_number_served(self):
#          return self.number_served
#
# if __name__=='__main__':
#     restaurant=[Restaurant('Harden','湘菜',10),
#                 Restaurant('KD','粤菜',2),
#                 Restaurant('James','鲁菜',5),
#                 Restaurant('CCSU__MI','湘菜',110),
#                 Restaurant('CCSU__Cola','苏菜',100)]
#     restaurant_max=Restaurant('','',0)
#     maxx=0
#     sum=0
#     for res in restaurant:
#         num=res.get_number_served()
#         sum+=num
#         if num>maxx:
#             maxx=num
#             restaurant_max=res
#     restaurant_list=[res for res in restaurant if res.get_number_served()>=10]
#     print("就餐人数最多的餐馆为:")
#     restaurant_max.describe_restaurant()
#     print('就餐人数大于等于10的餐馆为：')
#     for res in restaurant_list:
#         res.describe_restaurant()
#     print(f"所有餐馆就餐人数的总和为:{sum}")

# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name+" "+self.cuisine_type)
#
#     def open_restaurant(self):
#         print("餐馆正在营业中！！")
#
#     def set_number_served(self,number_served):
#         self.number_served=number_served
#
#     def get_number_served(self):
#         return self.number_served
#
#     def increment_number_served(self,number):
#         self.number_served+=number
#
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors=['Strawberry Ice Cream','Watermelon Ice Cream','Durian Ice Cream']
#
#     def show_flavors(self):
#         for ice in self.flavors:
#             print(ice)
#
# if __name__=='__main__':
#     ice=IceCreamStand('CCSU__MI','冰淇淋')
#     ice.show_flavors()

# from random import randint
# class Die():
#     def __init__(self,sides=6):
#         self.sides=sides
#
#     def roll_die(self):
#         print(randint(1, self.sides))
#
# if __name__=='__main__':
#     die1=Die()
#     for i in range(0,10):
#         die1.roll_die()
#
#     die2=Die(10)
#     for i in range(0,10):
#         die2.roll_die()
#
#     die3=Die(20)
#     for i in range(0,10):
#         die3.roll_die()

# import random
# num_list=list(range(10)) + ['m', 'i', 'h', 'a', 'b','n']
# number=random.sample(num_list,4)
# print(f"中奖号码为{number}")
# ans=0
# while True:
#     new_number=random.sample(num_list,4)
#     ans+=1
#     if new_number==number:
#         print(f"经过{ans}次终于中奖了")
#         break;

# class Money():
#     def __init__(self,amount,currency):
#         self.amount=amount
#         self.currency=currency
#
#     def __str__(self):
#         return '(Money: %s, %s)' % (self.amount, self.currency)
#
#     def __add__(self, other):
#         return Money(self.amount + other.amount,self.currency)
#
#     def __sub__(self, other):
#         return Money(self.amount - other.amount, self.currency)
#
#     def __mul__(self, other):
#         return Money(self.amount * other.amount, self.currency)
#
#     def __truediv__(self, other):
#         return Money(self.amount / other.amount, self.currency)
#
#     def __eq__(self, other):
#         return self.amount==other.amount
#
#     def __gt__(self, other):
#         return self.amount>other.amount
#
#     def __lt__(self, other):
#         return self.amount < other.amount
#
# if __name__=='__main__':
#     money1=Money(100,'人民币')
#     money2=Money(50,'人民币')
#     print(money1)
#     print(money2)
#     money1=money1+money2
#     print(money1)

# from dataclasses import dataclass
# @dataclass(init=True, repr=True, eq=True,order=True)
# class Money():
#     amount:int
#     currency:str
#
#     def __str__(self) -> str:
#         return '(Money: %s, %s)' % (self.amount, self.currency)
#
#     def __add__(self, other):
#         return Money(self.amount + other.amount,self.currency)
#
#     def __sub__(self, other):
#         return Money(self.amount - other.amount, self.currency)
#
#     def __mul__(self, other):
#         return Money(self.amount * other.amount, self.currency)
#
#     def __truediv__(self, other):
#         return Money(self.amount / other.amount, self.currency)
#
#     # def __eq__(self, other) -> bool:
#     #     return self.amount==other.amount
#     #
#     # def __gt__(self, other) -> bool:
#     #     return self.amount>other.amount
#     #
#     # def __lt__(self, other) -> bool:
#     #     return self.amount < other.amount
# if __name__=='__main__':
#     money1=Money(100,'人民币')
#     money2=Money(200,'人民币')
#     print(money1)
#     print(money2)
#     if money1>money2:print("money1")
#     else :print("money2")
#     money1=money1*money2
#     print(money1)




