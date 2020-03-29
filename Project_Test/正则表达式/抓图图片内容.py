# F:\project\Project_Test\正则表达式\img.html
import re
"""
1.下载页面的html
2.正则表达式匹配
<img.+src=\"(.+)\?.+

"""

def test_img():
    with open(r'F:\\project\\Project_Test\\正则表达式\\img.html','r',encoding='utf-8') as f:
        # while True:
        html=f.read()
            # if not html:
                # break
        #使用正则匹配找到所有的图片
        # pattent=re.compile(r'<img.+?src=\"(.+)\?.+?>|<img.+?data-original=\"(.+)\?.+?>',re.I|re.M)
        pattent=re.compile(r'<img.+?src=\"(.+?)\"')
        list_img=pattent.findall(html)
        for i in list_img:
            print(i)
        # print(len(list_img))

    

if __name__ == "__main__":
    test_img()