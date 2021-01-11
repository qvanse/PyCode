import re

"""
r2='\s{3}|\n' #德邦web导入


s='''沈阳   18740434666
陕西省/西安市/碑林区 友谊西路与水文巷交叉口，张老五东北铁锅炖'''
    
        
a=re.split(r2,s)#去除字符串前面和后面的所有设置的字符串

a.insert(1,' ')
for n in a:
    print(n,end='\t')
"""
s ="""
GET /download/1.0.0/group1/M00/A2/3F/wKgJN1vG236DvCPxAIV8Oj-LrmU250.m4a?buy_key=32313339373136343639&duration=1080&sign=38f67eb3cdc38506e844be0ccc5a2f7b&timestamp=1594533290&token=8519&uid=17069353&is_charge=true HTTP/1.1
Accept-Encoding: identity
RANGE: bytes=2359296-2424831
user-agent: ting_6.6.84(PBAM00,Android27)
Host: audiopay.cos.xmcdn.com
Connection: Keep-Alive"""
# li = s.split('"\r\n"') #注意：引号内有空格
# print (li)
print(s)