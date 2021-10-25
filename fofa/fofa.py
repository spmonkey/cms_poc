import base64,requests,time
from urllib import parse
from lxml import etree

def fofa(note):
    heading = {
        'cookie' : input('请输入cookie:')
    }
    url = 'https://fofa.so/'
    path = 'result?qbase64=' #狮子鱼"/seller.php?s=/Public/login"
    parameter = str(base64.b64encode(note.encode('utf-8')),"utf-8")    #对输入的参数进行base64编码
    parser = parse.quote(parameter)     #对base64再进行url编码
    page = '&page='
    #循环进行下一页爬取
    for pages in range(1,10):
        urls = url + path + parser + page + str(pages)          #合并链接
        print(urls)
        print('正在提取第'+str(pages)+'页')
        try:
            result = requests.get(url=urls,headers=heading).content #请求合并链接，.content中间存的是字节码
            # result = requests.get(url=urls).content
            # result = requests.get(url=urls, headers=heading).text   #.text存的是.content编码后的字符串
            # print(result.decode("utf-8"))
            # print(urls)
            # soup = BeautifulSoup(result,'lxml')
            soup = etree.HTML(result)   #进行HTML解析
            # soup1 = soup.find_all(re.compile("Error 500程序出错了!"))
            # print(soup)
            ip_path = soup.xpath('//span[@class="aSpan"]/a/@href')     #获取绝对地址的内容
            ip_data  = '\n'.join(ip_path)       #将序列中的元素以指定的字符连接生成一个新的字符串
            # print(ip_data)
            # print(result.decode(ip_data))       #输出字符串
            if ip_path != []:
            #循环写入文本
                with open(r'ip.txt','a+') as f:
                    f.write(ip_data + '\n')
            else:
                f.close()
                print('爬取完成！')
                print('准备验证poc！')
                time.sleep(0.5)
                pass
        except Exception as e:
            print('error',e)
            pass