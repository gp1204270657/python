from Project_Test.新闻系统.vega.dba.user_dao import UserDao

class UserService:
    
    user_dao=UserDao()

    #登录
    def login(self,username,password):
        result=self.user_dao.login(username,password)
        return result

    #返回查询的角色
    def seach_user_role(self,username):
        role=self.user_dao.seach_user_role(username)
        return role

    #新增用户
    def insert_user(self,username,password,email,role_id):
        self.user_dao.insert_user(username,password,email,role_id)

    # 查询用户的总数
    def seach_user_count(self):
        count_page=self.user_dao.seach_user_count()
        return count_page

    #查询用户列表
    def seach_user_list(self,page):
        result=self.user_dao.seach_user_list(page)
        return result

    #通过id删除用户
    def delete_by_id(self,id):
        self.user_dao.delete_by_id(id)

    #更新用户的信息
    def update_user(self,id,username,password,email,role_id):
        self.user_dao.update_user(id,username,password,email,role_id)



# if __name__ == "__main__":
#     u=UserService()
#     print(u.login("gp","123123"))
    