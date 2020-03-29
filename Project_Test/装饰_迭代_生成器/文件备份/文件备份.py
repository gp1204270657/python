import os
import os.path
import sys


class file(object):
    """
    构造函数，初始化要备份的文件，及备份后文件的路径
    src:原文件目录
    dic：备份后目录
    """

    def __init__(self, src, dic):
        self.src = src
        self.dic = dic
    """
    读取当前文件里面的内容
    """

    def read_file(self):
        ls = os.listdir(self.src)
        for i in ls:
            # 将遍历出的文件，加上完整的路径名字
            c_file = os.path.join(self.src, i)
            # 判断是否为文件夹，是文件夹就获取当前的路径为新的路径，递归查找
            if os.path.isdir(c_file):
                self.src = c_file
                # 利用递归函数
                self.read_file()

            self.copy_file(i)
    """
    备份文件操作
    """

    def copy_file(self, dic_path):
        # 1.选择需要备份文件的目录，不存在就创建
        if not os.path.exists(self.dic):
            os.makedirs(self.dic)
            print("指定目录不存在，已自动创建")

        # 2.备份的文件路径
        full_src_path = os.path.join(self.src, dic_path)
        full_dic_path = os.path.join(self.dic, dic_path)

        # 判断文件存在，且后缀为txt

        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1] == '.txt':
            with open(full_dic_path, "w", encoding="utf-8") as f_dic:
                with open(full_src_path, "r", encoding="utf-8") as f_src:
                    while True:
                        # 读取文件
                        res = f_src.read(100)
                        # 读取完了就跳出
                        if not res:
                            break
                        # 把读取的文件写入到路径下
                        f_dic.write(res)
                    f_dic.flush()


if __name__ == "__main__":

    # 通过os.path.abspath获得当前文件的绝对路径,os.path.dirname,获取目录的名称
    base_path = os.path.dirname(os.path.abspath(__file__))
    # os.path.join可以拼接新的路径地址
    src_path = os.path.join(base_path, 'src')
    dic_path = os.path.join(base_path, 'dic')
    f = file(src_path, dic_path)
    f.read_file()

