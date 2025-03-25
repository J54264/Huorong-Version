import requests
import json
from datetime import datetime

def fetch_data():
    url = "https://www.huorong.cn/versionShow.php"
    params = {"request_type": 1}
    response = requests.get(url, params=params)
    return json.loads(response.text)

def generate_table(data):
    table = """
## 版本信息

最后更新: {update_time}

| 架构    | 类型  | 病毒库版本 | 程序版本 | 生成时间 | 文件名 | 大小 | 下载链接 |
|---------|-------|------------|----------|----------|--------|------|----------|
""".format(update_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # x86/x64 架构
    table += "| x64     | Full | {virus} | {version} | {time} | {full_name} | {size} | [下载]({full_url}) |\n".format(
        virus=data['virusVersion'],
        version=data['version'],
        time=data['createtime'],
        full_name=data['fullName'],
        size=data['filesize'],
        full_url=data['urlFull']
    )
    table += "| x64     | All  | {virus} | {version} | {time} | {all_name} | {size} | [下载]({all_url}) |\n".format(
        virus=data['virusVersion'],
        version=data['version'],
        time=data['createtime'],
        all_name=data['allName'],
        size=data['filesize'],
        all_url=data['urlAll']
    )

    # ARM64 架构
    table += "| ARM64   | Full | {virus} | {version} | {time} | {full_name} | {size} | [下载]({full_url}) |\n".format(
        virus=data['virusVersion'],
        version=data['version'],
        time=data['createtime'],
        full_name=data['armFullName'],
        size=data['armFilesize'],
        full_url=data['armUrlFull']
    )
    table += "| ARM64   | All  | {virus} | {version} | {time} | {all_name} | {size} | [下载]({all_url}) |\n".format(
        virus=data['virusVersion'],
        version=data['version'],
        time=data['createtime'],
        all_name=data['armAllName'],
        size=data['armFilesize'],
        all_url=data['armUrlAll']
    )

    return table

def update_readme(table):
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换表格内容
    new_content = content.split('<!-- TABLE_START -->')[0] + \
        '<!-- TABLE_START -->\n' + table + '\n<!-- TABLE_END -->' + \
        content.split('<!-- TABLE_END -->')[1]

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    data = fetch_data()
    table = generate_table(data)
    update_readme(table)
