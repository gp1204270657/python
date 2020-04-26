#coding=utf-8
from Project_Test.新闻系统.vega.dba.mysql_db import pooldb
class UserDao(object):
    #登录验证有无数据
    def login(self,username,password):
        try:
            pool=pooldb.connection()
            cursor=pool.cursor()
            sql="SELECT COUNT(*) FROM t_user WHERE username=%s AND password=%s"
            cursor.execute(sql,(username,password))
            count=cursor.fetchone()[0]
            return True if count==1 else False
            
        except Exception as e:
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #查询用户的角色
    def seach_user_role(self,username):
        try:
            pool = pooldb.connection()
            cursor=pool.cursor()
            sql="SELECT r.role FROM t_user t JOIN t_role r on t.role_id=r.id WHERE t.username=%s"
            cursor.execute(sql,[username])
            role=cursor.fetchone()[0]
            return role
        except Exception as e:
            # pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    # 新增用户
    def insert_user(self, username, password, email, role_id):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "INSERT INTO t_user(username,password,email,role_id) VALUES(%s,%s,%s,%s)"
            cursor.execute(sql, (username,password,email,role_id))
            pool.commit()

        except Exception as e:
            if "pool" in dir():
                pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #查询用户的总数
    def seach_user_count(self):
        try:
            pool = pooldb.connection()
            cursor=pool.cursor()
            sql="SELECT CEIL(count(*)/10) from t_user"
            cursor.execute(sql)
            count_page=cursor.fetchone()[0]
            return count_page
        except Exception as e:
            # pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()


    #查询用户列表
    def seach_user_list(self,page):
        try:
            pool = pooldb.connection()
            cursor=pool.cursor()
            sql="SELECT u.id,u.username,t.role from "\
            "t_user u join t_role t on u.role_id=t.id "\
            "order by u.id "\
            "limit %s,%s"
            cursor.execute(sql,((page-1)*10,10))
            result=cursor.fetchall()
            return result
        except Exception as e:
            # pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #通过id删除用户
    def delete_by_id(self,id):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "delete from t_user where id=%s"
            cursor.execute(sql, [id])
            pool.commit()

        except Exception as e:
            if "pool" in dir():
                pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #更新用户的信息
    def update_user(self,id,username,password,email,role_id):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "update t_user set username=%s,password=%s,email=%s,role_id=%s where id=%s"
            cursor.execute(sql, (username,password,email,role_id,id))
            pool.commit()
        except Exception as e:
            if "pool" in dir():
                pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()





#
# if __name__ == "__main__":
#     u=UserDao()
#     print(u.seach_user_list(1))