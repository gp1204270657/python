from Project_Test.新闻系统.vega.serveice.user_service import UserService
from Project_Test.新闻系统.vega.serveice.news_service import News_Serivce
from Project_Test.新闻系统.vega.serveice.Role_service import Role_Service

from colorama import Style,Fore
import os,sys,time

user_service=UserService()
new_service=News_Serivce()
role_service=Role_Service()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX,"\n\t==========================")
    print(Fore.LIGHTBLUE_EX,"\n\t欢迎来到新闻管理系统")
    print(Fore.LIGHTBLUE_EX,"\n\t==========================")
    print(Fore.LIGHTGREEN_EX,"\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX,"\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt=input("\n\t请输入您的操作")

    if opt=="1":
        username=input("\n\t用户名：")
        password=input("\n\t密码：")
        #调用登录函数
        reslut=user_service.login(username,password)
        #登录成功
        if reslut==True:
            #查询身份
            role=user_service.seach_user_role(username)
            os.system("cls")
            while True:
                if role=="新闻编辑":
                    print("test")
                elif role=="管理员":
                    print(Fore.LIGHTGREEN_EX,"\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX,"\n\t2.用户管理")
                    print(Fore.LIGHTGREEN_EX,"\n\t3.退出登录")
                    print(Fore.LIGHTGREEN_EX,"\n\t4.退出系统")
                    print(Style.RESET_ALL)
                    opt=input("\n\t请选择操作")
                    if opt=="1":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作")
                            if opt=="1":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page=new_service.seach_unreview_count_page()
                                    print(count_page)
                                    reslut=new_service.seach_unreview_list(page)
                                    for index in range(len(reslut)):
                                        one=reslut[index]
                                        print(Fore.LIGHTGREEN_EX, "\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d"%(page,count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTGREEN_EX, "\n\tleft.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tright.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作")
                                    if opt=="back":
                                        break
                                    elif opt=="left" and page>1:
                                        page-=1
                                    elif opt=="right" and page<count_page:
                                        page+=1
                                    elif int(opt)>0 and int(opt)<11:
                                        news_id=reslut[int(opt)-1][0]
                                        new_service.update_unreview(news_id)
                            elif opt=="2":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page=new_service.seach_count()
                                    reslut=new_service.seach_list(page)
                                    for index in range(len(reslut)):
                                        one=reslut[index]
                                        print(Fore.LIGHTGREEN_EX, "\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d"%(page,count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTGREEN_EX, "\n\tleft.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tright.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作")
                                    if opt=="back":
                                        break
                                    elif opt=="left" and page>1:
                                        page-=1
                                    elif opt=="right" and page<count_page:
                                        page+=1
                                    elif int(opt)>0 and int(opt)<11:
                                        news_id=reslut[int(opt)-1][0]
                                        new_service.delete_by_id(news_id)
                            elif opt=="3":
                                break
                    elif opt=="2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作")
                            if opt=="back":
                                break
                            elif opt=="1":
                                os.system("cls")
                                username=input("\n\t请输入用户名：")
                                password = input("\n\t请输入密码：")
                                new_password= input("\n\t请输入确认密码：")
                                if password!=new_password:
                                    print("二次密码不一致,2秒后自动返回")
                                    time.sleep(2)
                                    continue
                                email = input("\n\t请输入邮箱：")
                                #查询当前的角色
                                result=role_service.seach_list()
                                for index in range(len(result)):
                                    one=result[index]
                                    print("\n\t%d.%s"%(index+1,one[1]))
                                opt= input("\n\t请分配编号：")
                                role_id=result[int(opt)-1][0]
                                user_service.insert_user(username,password,email,role_id)
                                print("添加成功,2秒后自动返回")
                                time.sleep(2)
                            elif opt=="2":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page=user_service.seach_user_count()
                                    result=user_service.seach_user_list(page)
                                    for index in range(len(result)):
                                        one=result[index]
                                        print(Fore.LIGHTGREEN_EX,"\n\t%d\t%s\t%s" % (index + 1, one[1],one[2]))
                                    print(Fore.LIGHTGREEN_EX,"\n\t%d/%d"%(page,count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tleft.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tright.下一页")
                                    print(Style.RESET_ALL)
                                    opt=input("\n\t请输入要修改的用户编号：")
                                    if opt=="back":
                                        break
                                    elif opt=="left" and page>1:
                                        page-=1
                                    elif opt=="right" and page<count_page:
                                        page+=1
                                    elif int(opt)>=1 and int(opt)<=10:
                                        os.system("cls")
                                        user_id=result[int(opt)-1][0]
                                        username= input("\n\t请输入用户名")
                                        password=input("\n\t请输入密码")
                                        new_password=input("\n\t请再次确认密码")
                                        if password!=new_password:
                                            print("\n\t二次密码不一致，2秒后自动返回")
                                            time.sleep(2)
                                            break
                                        email = input("\n\t请输入邮箱")
                                        result=role_service.seach_list()
                                        for index in range(len(result)):
                                            one=result[index]
                                            print("\n\t%d.%s" % (index + 1, one[1]))
                                        opt = input("\n\t请分配编号：")
                                        role_id=result[int(opt)-1][0]
                                        opt=input("\n\t请确认是否保存Y/N？")
                                        if opt=="Y" or opt=="y":
                                            user_service.update_user(user_id,username,password,email,role_id)
                                            print("\n\t修改成功，2秒后自动返回")
                                            time.sleep(2)
                                            break
                            elif opt=="3":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = user_service.seach_user_count()
                                    result = user_service.seach_user_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX, "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tleft.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tright.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作：")
                                    if opt == "back":
                                        break
                                    elif opt == "left" and page > 1:
                                        page -= 1
                                    elif opt == "right" and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10:
                                        os.system("cls")

                                        uid = input("\n\t请输入要删除的用户id")
                                        user_id = result[int(uid) - 1][0]
                                        opt = input("\n\t请确认是否保存Y/N？")
                                        if opt == "Y" or opt == "y":
                                            user_service.delete_by_id(user_id)
                                            print("\n\t删除成功，2秒后自动返回")
                                            time.sleep(2)
                                            break


                    elif opt=="3":
                        break
                    elif opt=="4":
                        print("\n\t退出成功欢迎下次再来！")
                        sys.exit(0)

        else:
            print("\n\t用户名或密码错误，2秒后自动返回")
            time.sleep(2)
    elif opt=="2":
        print("\n\t退出成功欢迎下次再来！")
        sys.exit(0)