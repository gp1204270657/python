
"""
@staticmethod  表示静态的方法，在方法名上方添加，直接用类名.方法名调用
@classmethod   表示类的引用对象
"""

class Person(object):

    #将类及属性设置为静态的方法，无法添加或修改参数
    __slots__={"name","title"}
    
    def __init__(self,name):
        self.name=name
      
    
    def speak_1(self):
        res="我的名字是{0},我是一个演说家，".format(self.name)
        print(res)
        return res
       
       

class Spaker(object):
    def __init__(self,title):
        self.title=title

    def speak_2(self):       
        res="我演讲的主题是{0}".format(self.title)
        print(res)
        return res
    

class Student(Spaker,Person):
    def __init__(self,name,title):
        #继承多个父类，初始化的时候需要将父类的应用
        Person.__init__(self,name)
        Spaker.__init__(self,title)
    

        
#前往别忘记在类中所有的方法需要添加self这个参数
    def test(self):
        if issubclass(Student,Person):
            print("Student是Person子类")
        if issubclass(Student,Spaker):
            print("Student是Spaker子类")

if __name__ == "__main__":
    s=Student("john","python")
    s.speak_1()
    s.speak_2()
    s.test()
