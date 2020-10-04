import requests
import time
from pygame import mixer

def play(audio_path):
    mixer.init()
    mixer.music.load(audio_path)
    mixer.music.play()
    
def get_a_list_of_projects(keyword):
    list_route = '/public/project/list'
    list_url = base_url + list_route
    params = {
        'page' : '1',
        'limit' : '100',
        'keyword' : keyword,
        'apikey' : apikey,
    }
    response = requests.get(list_url, params=params, headers=headers).json()
    list_data = response['data']
    for i in range(len(list_data)):
        list = list_data[i]
        supportCountry = list['supportCountry']
        cnname = list['cnname']
        sellingPrice = list['sellingPrice']
        myPid = list['myPid']
        print(f'渠道名：{cnname}，价格：{sellingPrice}，myPid：{myPid}，国家选择：{supportCountry}')
            
def get_the_number_of_projects_count():
    pass

def get_number(sel_myPid, sel_locale):
    number_route = '/public/sms/getNumber'
    number_url = base_url + number_route
    params = {
        'myPid': sel_myPid,
        'locale': sel_locale,
        'apikey': apikey
    }
    n = 1
    while True:
        response = requests.get(number_url, params=params, headers=headers).json()
        if response['code'] == 1:
            play('./获得道具.mp3')
            break
        else:
            print(response)
            print(f'第{n}次请求号码失败')
            n += 1
            time.sleep(0.5)
    return response['data']

def get_verification_code(orderId):
    veri_route = '/public/sms/getCode'
    veri_url = base_url + veri_route
    params = {
        'orderId': orderId,
        'apikey': apikey,
    }
    n = 1
    while True:
        response = requests.get(veri_url, params=params, headers=headers).json()
        if response['code'] == 1:
            break
        else:
            print(response)
            print(f'第{n}次请求验证码失败')
            n += 1
            time.sleep(0.5)
    return response['data']

def release_number(orderId):
    release_route = '/public/sms/releaseNumber'
    release_url = base_url + release_route
    params = {
        'orderId': orderId,
        'apikey': apikey,
    }
    n = 1
    while True:
        response = requests.get(release_url, params=params, headers=headers).json()
        if response['code'] == 1:
            break
        else:
            print(response)
            print(f'第{n}次释放号码失败')
            n += 1
            time.sleep(0.5)
    return response['data']

def get_user_information():
    info_route = '/public/user/info'
    info_url = base_url + info_route
    params = {
        'apikey': apikey
    }
    response = requests.get(info_url, params=params, headers=headers).json()
    info_data = response['data']
    infoUsername = info_data['username']
    infoBalance = info_data['balance']
    print(f'用户名：{infoUsername}，余额：{infoBalance}')

if __name__ == "__main__":
    base_url = 'http://www.jindousms.com'
    apikey = 'cbeda47e5041edc146b3f3d0bfce1e54'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68'
    }

    while True:
        choice = input('是否开始请求号码？\n1. 查询渠道代码\n2. 开始请求下一个号码\n3. 查询账户信息\n4. 退出当前程序\n')
        if choice == '1':
            keyword = input('请输入查询关键词：')
            get_a_list_of_projects(keyword)
        elif choice == '2':
            sel_myPid = input('请输入需要选择的渠道代码myPid：')
            sel_locale = input('请输入需要选择的国家缩写：')
            number_data = get_number(sel_myPid, sel_locale)
            orderNumber = number_data['number']
            orderId = number_data['orderId']
            print(f'本次请求到的号码为：{orderNumber}')
            sel = input('是否开始请求验证码？\n1. 开始请求验证码\n2. 释放当前号码\n')
            if sel == '1':
                veri_data = get_verification_code(orderId)
                veriCode = veri_data['code']
                veriContent = veri_data['content']
                print(f'本次请求到的验证码为：{veriCode}')
                get_user_information()
            elif sel == '2':
                release_data = release_number(orderId)
                print(f'释放号码成功，返回数据标识：{release_data}')
                get_user_information
        elif choice == '3':
            get_user_information()
        elif choice == '4':
            break

