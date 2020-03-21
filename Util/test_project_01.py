#coding=utf-8:
flag=True
server_menu={'1':'人民币转换美元',2:"美元转换人民币",3:"人民币转换欧元",0:"结束程序"}
#文案的获取
def wenan():
    print('**********欢迎使用货币转换系统************')
    for k,v in server_menu.items():
        print(k,'.',v)
#实现程序的循环
def xunhuan():
    while flag:
        wenan()
        ste=input('请选择你需要的服务')
        if  int(ste)==1:
            print("欢迎使用人民币兑换系统")
            money=input("请输入兑换的金额：")
            print("你输入的金额为",float(money))
            usa=int(money)/6.72
            print("兑换成美元为",round(float(usa),2),"$")
            xunhuan()
        elif int(ste)==0:
            print("程序结束")
            break
        else：
         



if __name__ == "__main__":
    xunhuan()

