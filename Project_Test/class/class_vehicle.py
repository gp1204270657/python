class Vehicle(object):
    tag="SUV"
    """
    初始化速度跟大小尺寸
    """
    def __init__(self,speed,size=(10,20,30)):
        self.speed=speed
        self.size=size
    
    def show_info(self):
        res="我的车型是{0}，当前的速度是{1}KM/h，尺寸大小是{2}".format(self.tag,self.speed,self.size)
        print(res)
        return res
#设置新的移动速度
    def set_speed(self,speed):
        self.speed=speed
        
    
    def get_speed(self):
        print("加速了---",self.speed)
        return self.speed

    def move(self):
        print("我已经向前移动50米")
    
    def speed_up(self,num):
        speed=self.speed+num
        print("我的速度提升了{0}，当前速度是{1}".format(num,speed))
        
    def transport(self,x,y):
        if isinstance(x,y):
            print("是他的子类")

if __name__ == "__main__":
    v=Vehicle(20)
    v.show_info()
    v.move()
    print("---------------------")
    v.set_speed(80)
    v.get_speed()
    v.show_info()
    v.transport(v,Vehicle)
    v.speed_up(10)
