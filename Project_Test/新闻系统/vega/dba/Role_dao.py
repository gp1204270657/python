from Project_Test.新闻系统.vega.dba.mysql_db import pooldb

class RoleDao:
    #查询所有角色
    def seach_list(self):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "SELECT id,role from t_role"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

