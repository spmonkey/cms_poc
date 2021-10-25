# -*- coding : utf-8 -*-
# -*- developer : F -*-
from fofa_poc.sql_poc.sql import cms_poc
from fofa_poc.fofa.fofa import fofa
from fofa_poc.upload_poc.upload import *
import argparse,urllib3

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
