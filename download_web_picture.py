import re
import os
import time

try:
    import requests 
except ImportError:
    print("Trying to Install required module: requests\n")
    os.system('pip install requests')

def prompt(msg):
    """提示信息
    """
    print('='.center(20, '='))
    print(msg)
    print('='.center(20, '='))

def download(results: list):
    """下载图片
    """
    prompt('开始下载图片!!')
    path = input('请输入图片保存路径:\n').strip()

    j = 0
    for result in results:
        print('正在保存第{}个'.format(j))
        try:
            pic = requests.get(result, timeout=10)
            # time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        # 把图片保存到文件夹
        file_full_name = os.path.join(path, result.split('/')[-1])
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)
            f.close()

        j += 1

def main():
    """下载
    """
    prompt('开始下载网站图片!!')
    url = input('请输入网址:\n').strip()

    # 发送请求，获取相应
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}
    response = requests.get(url, headers=headers)
    html = response.content.decode()

    prompt('开始提取图片地址!!')
    results = re.findall('img src=".+[pn,jp,jpe]g"', html)
    imgs = []
    for one_result in results:
        v = one_result.split('./')
        if len(v) >= 2:
            imgs.append(url+v[1][0:-1])

    print(imgs)

    # 下载图片
    download(imgs)

if __name__ == "__main__":
    main()