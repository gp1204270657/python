
def test_read():

    file_name="F:\\Study\\studypy\\python\\Project_Test\\文件读写\\test.txt"
    #open()打开文件
    f=open(file_name,encoding='utf-8')
    #读取指定的数量
    # res=f.read(5)
    # print(res)
    #读取一行
    # res=f.readline()
    # print(res)
    #读取一行，返回一个列表
    res=f.readlines()
    print(res)
    f.close()

if __name__ == "__main__":
    test_read()