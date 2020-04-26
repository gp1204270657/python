from Project_Test.新闻系统.vega.dba.Role_dao import RoleDao

class Role_Service:
    role_dao=RoleDao()

    # 查询所有角色
    def seach_list(self):
        result=self.role_dao.seach_list()
        return result