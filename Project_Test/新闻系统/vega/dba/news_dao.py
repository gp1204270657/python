# coding=utf-8
from DBUtils.PooledDB import PooledDB
from Project_Test.新闻系统.vega.dba.mysql_db import pooldb


class NewsDao(object):

    #查询新闻列表
    def seach_list(self,page):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql ="SELECT n.id,n.title,t.type,u.username " \
                 "FROM t_news n JOIN t_type t on n.type_id=t.id JOIN t_user u on " \
                 "n.editor_id=u.id " \
                  "ORDER BY create_time DESC " \
                "LIMIT %s,%s"
            cursor.execute(sql,((page-1)*10,10))
            result= cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "pool" in dir():
                pool.close()


    #查询待审批的列表数据
    def seach_unreview_list(self, page):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql ="SELECT n.id,n.title,t.type,u.username " \
                 "FROM t_news n JOIN t_type t on n.type_id=t.id JOIN t_user u on " \
                 "n.editor_id=u.id " \
                  "WHERE n.state=%s " \
                  "ORDER BY create_time DESC " \
                "LIMIT %s,%s"
            cursor.execute(sql,("待审批",(page-1)*10,10))
            result= cursor.fetchall()
            return result

        except Exception as e:
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #查询待审批状态的总页数
    def seach_unreview_count_page(self):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) from t_news where state=%s"
            cursor.execute(sql, ["待审批"])
            count_page = cursor.fetchone()[0]
            return count_page

        except Exception as e:
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #查询新闻的总页数
    def seach_count(self):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) from t_news "
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page

        except Exception as e:
            print(e)
        finally:
            if "pool" in dir():
                pool.close()



    #审批新闻
    def update_unreview(self,id):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "update t_news set state=%s where id=%s"
            cursor.execute(sql, ("已审批",id))
            pool.commit()

        except Exception as e:
            if "pool" in dir():
                pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()

    #删除新闻
    def delete_by_id(self,id):
        try:
            pool = pooldb.connection()
            cursor = pool.cursor()
            sql = "delete from t_news where id=%s"
            cursor.execute(sql, [id])
            pool.commit()

        except Exception as e:
            if "pool" in dir():
                pool.rollback()
            print(e)
        finally:
            if "pool" in dir():
                pool.close()




# new=NewsDao()
# print(new.seach_unreview_list(1))