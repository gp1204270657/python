
class Cat(object):
    tag = "家猫"
    '''
    猫科动物类
    '''

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        pass

    def set_age(self, age):
        """
        设置年龄
        """
        self.__age = age

    #描述符，类的方法直接调用,下方调用该方法的时候不需要加括号
    @property
    def show_info(self):
        res = "我叫{0}，今年{1}岁".format(self.name, self.__age)
        print(res)
        return res

    def catch(self):
        print("猫咪会抓老鼠")

    def eat(self):
        print("猫爱吃鱼")


if __name__ == "__main__":
    cat_black=Cat('小黑',2)
    cat_black.eat()
    cat_black.show_info
    cat_black.set_age(5)
    cat_black.show_info
    print("------------")
    print(cat_black.name)
    # print(cat_black.__age)#前面加二个下划线的，代表私有的变量，无法改变及获取

    #判断是否是类的实例
    print(isinstance(cat_black,Cat))

