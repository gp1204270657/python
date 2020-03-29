#语法含有yield就一定是一个生成器
class Num():

    def num1(self):
        yield 1
        yield 2
        yield 3
        yield 4

    def num2(self):
        for i in [1,2,3,4,5,6]:
            yield i*i

    def num3(self,a=None,b):
        while True:
            if a==None:
                a=0
            print(a)
            a+=1
            if a>=b:
                return a

        
       



if __name__ == "__main__":
    n=Num()
    # rest=n.num2()
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # for i in rest:
    #     print(i)
    n.num3(6)