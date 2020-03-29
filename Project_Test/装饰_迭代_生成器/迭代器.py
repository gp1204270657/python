#通过next（）方法返回下一个值


class PetNumber(object):
    values=0
#返回1,2,3,4,5.。。的平方值
    def __next__(self):
        self.values+=1
        if self.values>10:
            raise StopIteration
        return self.values*self.values

#先定义一个迭代器
    def __iter__(self):
        return self


if __name__ == "__main__":
    p=PetNumber()
    # print(p.__next__())
    # print(p.__next__())
    # print(p.__next__())
    print(next(p))
    print(next(p))
    print(next(p))