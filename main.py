import requests

proxies = {
    'http': 'http://127.0.0.1:9999',
    'https': 'http://127.0.0.1:9999'
}
#創作者ID---------------------------
# user_id = '4196200'
user_id = input("請輸入userid:")
#取創作者網站---------------------------
url = f"https://www.pixiv.net/ajax/user/{user_id}/profile/all"
#創作者網站header
headers = {'HOST': 'www.pixiv.net',
           'accept': 'application/json',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
#創作者網站cookies---------------------------
cookies = {'PHPSESSID': '11769690_iOkEcjk4ZBQO4hJ4EGakkb297LgH6lJK'}
#對創作者作品網站發送請求
# res = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies, verify=False)
res = requests.get(url=url, headers=headers, cookies=cookies)
json_object = res.json()
#獲取該創作者所有圖片ID
work_id_list = list(json_object['body']['illusts'].keys())

#作品集header
header2 = {
    'Host': 'i.pximg.net',
    'Referer': 'https://www.pixiv.net/'
}

for i in work_id_list:
    url_work = f'https://www.pixiv.net/ajax/illust/{i}/pages' #取得圖片
    # res_more_img = requests.get(url=url_work, headers=headers, proxies=proxies, verify=False)
    res_more_img = requests.get(url=url_work, headers=headers)

    body = res_more_img.json()['body']
    header2 = {
        'Host': 'i.pximg.net',
        'Referer': 'https://www.pixiv.net/'
    }
    for item in body:
        urls = item['urls']['original']
        # res_img = requests.get(url=urls, headers=header2, proxies=proxies, verify=False)
        res_img = requests.get(url=urls, headers=header2)
        name = urls.split('/')[-1]
        # print(name)
        with open(f'img/{name}', 'wb') as f:
            f.write(res_img.content)

# res2 = requests.get(headers=header2,proxies=proxies, verify=False)

