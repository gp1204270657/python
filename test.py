#coding=utf-8
# list=[1,2,3,4,5,6,7,8,9,10]
# count=1
# for l in list:
#     if l%2==0:
#         print("di{0}geshi".format(count),l)
#         count+=1


#字典的运用
stre="213,jack,50&214,guozuji,100&215,caoshujian,250"
stre_list=stre.split('&')
all_dict={}

for k in stre_list:
    v_list=k.split(',')
    #创建员工列表
    e={'no':v_list[0],'name':v_list[1],'money':v_list[2]}
    all_dict[e['no']]=e
    print(all_dict)

#元祖的运用

t=(1,2,3,4)
print(t[2])

#生成式
lst=[]
for i in range(10,20):
    lst.append(i*10)
print(lst)
#列表生成式
lst2=[i*10 for i in range(10,20)]
print(lst2)
#字典生成式
lst3=['账上','你是','万物']
dic={i+1:lst3[i] for i in range(0,len(lst3))}
print(dic)

#集合生成式
set1={i*j for i in range(1,4) for j in range(1,4) if i==j }
print(set1)
for i in range(1,4) :
    for j in range(1,4):
        if i==j:
            set1.add(i*j)

lst3 = [23, 45, 22, 44, 25, 66, 78]
lst4=[lst3[i] for i in range(0,len(lst3)) if lst3[i]%2!=0]
print(lst4)




def login(username,password):
    if username=="imooc" and password=="123456":
        print("login success")
    else:
        print("login fail")
login("imooc","123456")
