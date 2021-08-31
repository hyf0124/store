# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for key in dict.keys():
#     print(key)
# for value in dict.values():
#     print(value)
# dict ['k4'] = 'v3'
# print(dict)



# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }

# Friuts = {'苹果':12.3,
#           '草莓':4.5,
#           '香蕉':6.3,
#           '葡萄':5.8,
#           '橘子':6.4,
#           '樱桃':15.8}
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money': 0
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money': 0
#     }
# }
# ming=info['小明'].get('fruits')
# gang=info['小刚'].get('fruits')
# def count(price):
#     global Friuts
#     money=0
#     for key, value in Friuts.items():
#         for name,count in price.items():
#             if key == name:
#                 money = money+(value*count)
#     return money
# info['小明']['money']=count(ming)
# info['小刚']['money']=count(gang)
# print(info)


# import random
#
# list=[]
# for i in range (50):
#     list.append(random.randint(1,50))
#
# print (list)
# from collections import Counter
# list = dict(Counter(list))
# print({key:value for key,value in list.items() if value > 1})




# from collections import Counter
# List = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
# list = dict(Counter(List))
# print({key:value for key,value in list.items() })


# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# p={}
# for i in names:
#     information={'姓名':i[0],'年龄':i[1],'性别':i[2],'编号':i[3],'任职公司':i[4],'薪资':i[5],'部门编号':i[6]}
#     p[i[0]]=information
# print(p)







