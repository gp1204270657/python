
class Animal(object):
    # pass
    # def __init__(self,name):
    #     self.name=name

    def eat(self):
        print("我爱吃食物")

    
#继承父类
class Cat(Animal):
    def eat(self):
        #调用父类的方法
        super().eat()
        print("我爱吃鱼")

#继承父类
class HuaCat(Cat):
    def eat(self):
        super().eat()
        print("我啥都吃")


if __name__ == "__main__":   
    cat_b=HuaCat()
    cat_A=Cat()
    print(issubclass(HuaCat,Cat))
    cat_b.eat()
