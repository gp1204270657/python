#coding=utf-8
import random

phone_str="火警【119】,急救【120】,警察[110],火车票【12306】"
witer_str="上海,18-36度,晴天~北京,23-37度,阴天"

#生成随机双色球的
def get_uinition(number):
     for j in range(0,int(number)):
            for i in range(0,6):
                red=random.randint(1,33)
                print(red,end=" ")
            blue=random.randint(1,16)
            print(blue)
#生成号码百事通
def phone_find(n):
    phone_list=phone_str.split(",")
    for i in phone_list:
        if i.find(n)!=-1:
            print(i)
        else:
            print("暂时没找到！")
            break
#生成天气查询
def werther_find(city):
    weather_data={}
    city_list=witer_str.split("~")
    for i in range(0,len(city_list)):
        w=city_list[i].split(",")
        weather={"name":w[0],"data":w[1],"wind":w[2]}
        weather_data[weather["name"]]=weather
    if city in weather_data:
        return weather_data.get(city)
    else:
        return {}


  




while True:
    print("1.双色球随机号码")
    print("2.百事通查询")
    print("3.天气预报信息")
    print("0.结束程序")
    c=input("请输入你要选择的选项")

    if c=="1":
        n=input("请输入要买几注:")
        get_uinition(n)
       
    elif c=="2":
        n=input("请输入要查询的诚实电话或关键字")
        phone_find(n)
      
    elif c=="3":
        city=input("请输入要查询的城市")
        w=werther_find(city)
        if "name" in w:
            print("{name} {data} {wind}".format_map(w))
        else:
            print("未找到{0}的信息".format(city))
    elif c=="0":
        break
    else:
        print("您输入的有误，请重新输入！")
print("程序结束感谢领您的使用，祝您生活愉快，再见！")
    
