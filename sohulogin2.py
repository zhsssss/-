# -*- coding: utf-8 -*-
# @Time : 2023/4/10 11:08
# @Author : zhi
# @File : sohulogin2
import time
import requests
import hashlib
def get_gidinf():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }
    params = {
        'r': 'http://s.m.sohu.com/h5apps/t/cn/428/600428.html?',
    }
    response = requests.get('http://h5.passport.sohu.com/app/login', params=params, headers=headers, verify=False)
    return response.cookies.get_dict()
def login(cookies,user,psw):
    t = int(time.time()*1000)
    cookies['t'] = str(t)
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://h5.passport.sohu.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://h5.passport.sohu.com/app/login?r=http%3A%2F%2Fs.m.sohu.com%2Fh5apps%2Ft%2Fcn%2F428%2F600428.html%3Fspm%3Dsmwp.content-n.content-n.2.16808900456642BKdaMY',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        't': f'{t+100}',
    }
    data = {
        'userid': f'86-{phone_number}',
        'password': f'{psw}',
        'appid': '',
    }
    response = requests.post(
        'http://h5.passport.sohu.com/security/login',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    print(response.text)
if __name__ == '__main__':
    cookies = get_gidinf()
    time.sleep(5)
    phone_number = 18000000000
    password = '12345678'
    md5_password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()
    login(cookies,user=phone_number,psw =password)