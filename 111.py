import requests
import re
url='https://tieba.baidu.com/p/2264641338'
wb_date = requests.get(url).text
res = re.compile(r'src="(http.+?jpg)"')
reg = re.findall(res,wb_date)

nun=0
for i in reg:
    print(i)
    a = requests.get(i)
    f =open('%s.jpg'%nun,'wb')
    f.write(a.content)
    f.close()
    nun=nun+1
    print('第%s个图片下载完毕'%nun)