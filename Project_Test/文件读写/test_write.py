import random
import datetime
def test_write():
    #写入单行的文件的内容
    file_name="F:\\Study\\studypy\\python\\Project_Test\\文件读写\\test_write.txt"
    with open(file_name,'w',encoding='utf-8') as f:
        f.write("hello")
        f.write("\n")
        f.write("world")

def test_write_lines():
    #写入多行文件的内容
     file_name="F:\\Study\\studypy\\python\\Project_Test\\文件读写\\test_write_lines.txt"
     l=['第一','\n','第二','\n','盖伦']
     with open(file_name,'w',encoding='utf-8') as f:
         f.writelines(l)
    
def test_write_user():
    #追加写入方式
    file_name="F:\\Study\\studypy\\python\\Project_Test\\文件读写\\test_write_user.txt"
    rest='用户的id{0}和时间{1}'.format(random.randint(10000,99999),datetime.datetime.now())
    # print(rest)
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(rest)
        f.write('\n')

def read_and_write():
    #读取跟写入同时操作
    file_name="F:\\Study\\studypy\\python\\Project_Test\\文件读写\\read_and_write.txt"
    with open(file_name,"r+",encoding='utf-8') as f:
        rest=f.read()
        if "0" in rest:
            f.write('hell')
        else:
            f.write('hello000')

        
if __name__ == "__main__":
    # test_write()
    # test_write_lines()
    # test_write_user()
    read_and_write()