# -*- coding : utf-8 -*-
# -*- developer : F -*-
from fofa_poc.sql_poc.sql import cms_poc
from fofa_poc.fofa.fofa import fofa
from fofa_poc.upload_poc.upload import *
import argparse,urllib3

# parser = argparse.ArgumentParser(description='This is the help!')
# parser.add_argument('-u','--url',help='单个检测',default='')
# parser.add_argument('-f','--file',help='多个检测',default='')
# urllib3.disable_warnings()
# args = parser.parse_args()

name = '''
   _______            ___         ___            _______
  / ______|          / _ \       / _ \          /  _____| 
 | (                / / \ \     / / \ \         | (_____
 | |               / /   \ \   / /   \ \        \_____  )
 | (______        / /     \ \_/ /     \ \        _____) |
  \ ______|      /_/       \___/       \_\      |______ /
  
'''
print(name)

if __name__ == "__main__":
    with open('E://note.txt','r') as a:
        notes = a.readlines()
        # print(len(notes))
        for i in notes:
            note = i.strip()
            fofa(note)
    with open('ip.txt','r') as p:
        results = p.readlines()
        # print(len(results))
        for result in results:
            if "http" in result:
                url = result.strip()
                # upload_poc(url)
                cms_poc(url)
            else:
                url = "http://" + result
                url = url.strip()
                # upload_poc(url)
                cms_poc(url)
    with open('ip.txt','r') as u:
        upload_pocs = u.readlines()
        for upload_poc in upload_pocs:
            upload(upload_poc)
    # if args.url !="" and args.file =="":
    #     upload(args.url)
    # if args.url =="" and args.file !="":
    #     more_upload(args.file)