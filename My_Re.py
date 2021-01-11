import re

# """
# r2='\s{3}|\n' #德邦web导入


# s='''沈阳   18740434666
# 陕西省/西安市/碑林区 友谊西路与水文巷交叉口，张老五东北铁锅炖'''
    
        
# a=re.split(r2,s)#去除字符串前面和后面的所有设置的字符串

# a.insert(1,' ')
# for n in a:
#     print(n,end='\t')
# """
url='http://audiopay.cos.xmcdn.com'
s ="""GET /download/1.0.0/group1/M0A/CD/3B/wKgJMlvUh26zlD-sAJjAtEkrrZQ972.m4a?buy_key=32303830303037373532&duration=1236&sign=775624163f963d2d67286d1da2129ec7&timestamp=1594980763&token=9070&uid=17069353&is_charge=true HTTP/1.1
Accept-Encoding: identity
RANGE: bytes=1114112-1179647
user-agent: ting_6.6.85(PBAM00,Android27)
Host: audiopay.cos.xmcdn.com
Connection: Keep-Alive"""
# s= input("input:")
li = s.split("\n") #注意：引号内有空格
li2=li[0].split()
li3=url+li2[1]
print (li3)

# print(s)