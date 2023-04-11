import requests  # 导入requests包

# 指定url为目标站点
url = 'https://www.yinfans.me/'
kw = input('请输入电影名关键字：')
param = {
    's':kw
}

# UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0'
}

# 1.发起请求
response = requests.get(url=url,params=param,headers=headers)

# 2.获取响应数据
page_text = response.text   # 设置变量page_text来保存网站数据为text格式

# 3.存储数据
with open('./yinfans.html','w',encoding="UTF-8") as fp:
    fp.write(page_text)
print('爬取数据结束，保存成功')
