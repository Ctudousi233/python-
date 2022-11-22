# 需求：爬取edge首页
import requests

if __name__ == '__main__':
    # step_1：指定url
    url = 'https://cn.bing.com/?scope=web&FORM=ANSPH1&pc=U531'
    # step_2：发起请求
    # get方法返回一个响应对象
    response = requests.get(url=url)
    # step_3：获取相应请求 .text返回的是字符串型的响应数据
    page_text = response.text
    print(page_text)
    # step_4：持久化存储
    with open('./edge.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')
