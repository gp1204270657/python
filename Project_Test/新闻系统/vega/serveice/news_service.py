from Project_Test.新闻系统.vega.dba.news_dao import NewsDao


class News_Serivce:

    news=NewsDao()

    # 查询新闻列表
    def seach_list(self, page):
        result=self.news.seach_list(page)
        return result

    # 查询待审批的列表数据
    def seach_unreview_list(self,page):
        result=self.news.seach_unreview_list(page)
        return result

    # 查询待审批状态的总页数
    def seach_unreview_count_page(self):
        count_page=self.news.seach_unreview_count_page()
        return count_page

    # 查询新闻的总页数
    def seach_count(self):
        count_page=self.news.seach_count()
        return count_page

    # 审批新闻
    def update_unreview(self, id):
        self.news.update_unreview(id)

    #删除新闻
    def delete_by_id(self,id):
        self.news.delete_by_id(id)
